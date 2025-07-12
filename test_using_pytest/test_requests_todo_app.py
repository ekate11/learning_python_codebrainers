import requests
import random
random.randint(10000,99999)


ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    code_response = response.status_code
    assert code_response==200

def test_api_returns_404_for_bad_url():
    response = requests.get(url=ENDPOINT +"/status")
    assert response.status_code == 404

def test_api_returns_hello_msg():
    """Body should return hello world message
    "message":"https://todo.pixegami.io"""

    response = requests.get(url=ENDPOINT)
    body = response.json()
    expected = "Hello World from Todo API"
    print(body)
    print(expected)
    assert expected == body["message"]

def test_api_returns_not_found_for_bad_url():
    """1. get response for GET(link)
    2. get body from response
    3. body should contain "Not Found"
    body: {"detail":"Not Found"}"""
    response = requests.get(url=ENDPOINT +"/status")
    body = response.json()
    expected = "Not Found"
    print(body)
    print(expected)
    assert expected == body["detail"]


def test_api_returns_not_found_for_bad_url():
    """
    1. get response for GET https://todo.pixegami.io/status
    2. get body from response
    3. body should contain "Not Found"
    body: {"detail":"Not Found"}
    """
    bad_url = ENDPOINT + "/nieistnieje"
    response = requests.get(bad_url)
    body = response.json()
    expected = {"detail":"Not Found"}
    assert expected == body


def test_can_create_task():
    """PUT https://todo.pixegami.io/status + body"""
    request_body = {
                    "content": "Nakarm kota",
                    "user_id": "Katimakota",
                    "task_id": "02",
                    "is_done": False
                    }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=request_body)
    assert response_put.status_code == 200

    response_body = response_put.json()
    print(response_body)
    res_user_id = response_body["task"]["user_id"]
    res_content = response_body["task"]["content"]
    res_is_done = response_body["task"]["is_done"]
    assert res_is_done == False
    assert res_user_id == "Katimakota"
    assert res_content == "Nakarm kota"


    # pytest -sv nastepne sciezka do testu zeby pokazal printy


def test_can_get_task():
    """GET https://todo.pixegami.io/get-task/{task-id} + body"""
    response = requests.get(url = ENDPOINT + "/get-task/" + "task_3acdc3ccdb814420aa31b8ee0cf829fc")
    assert response.status_code == 200
       
    body = response.json()
    print (body)

def test_not_existing_task_id_returns_404():
    response = requests.get(url=ENDPOINT + "/get-task/" + "task_3ertyui6789") 
    assert response.status_code == 404


def test_can_create_and_get_task():
    """GET https://todo.pixegami.io/get-task/{task-id} 
    1. create tsk
    2. extract task_id
    3. use unique_task_id from 2. to test get-task
    """
#1
    task_body = {
                    "content": "Nakarm kota",
                    "user_id": "Katimakota",
                    "task_id": "02",
                    "is_done": False
                    }
    response_create = requests.put(url=ENDPOINT +"/create-task", json=task_body)
    assert response_create.status_code == 200
#2
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]
    print("\n")
    print(unique_task_id)

#3
    response = requests.get(url = ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 200
    assert response.json()['task_id'] == unique_task_id
    print(unique_task_id)


def test_can_list_task():
    response = requests.get(url=ENDPOINT + "/list-tasks/Katimakota")
    assert response.status_code == 200

    body = response.json()
    print(body)



def test_can_list_tasks():
    """GET https://todo.pixegami.io/list-tasks/Alamakota_tmp2
    Napisz test do wylistowania tasks
    """
    radom_user = "Alamakota_tmp_" + str(random.randint(1000000, 9999999))
    task_body = {"content": "Nakarm kota",
                 "user_id": radom_user,
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200

    response = requests.get(url=ENDPOINT + "/list-tasks/" + radom_user)
    assert response.status_code == 200

    body = response.json()
    tasks = body["tasks"]
    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_can_update_task():
    """
    1. create task
    2. update task
    3. check if updated
    """
    #1
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_1",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]

    #2
    updated_body = {"content": "Nakarm kota",
                    "user_id": "Alamakota_1",
                    "task_id": unique_task_id,
                    "is_done": True
                    }
    response_update = requests.put(url=ENDPOINT + "/update-task", json=updated_body)
    assert response_update.status_code == 200

    #3
    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 200
    body = response.json()
    assert body["is_done"] == True

def test_can_delete_task():
    """
    1. create task
    2. extract task_id
    3. delete task
    4. get task and expect deleted
    """
    #1.
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_1",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    #body_create_response = response_create.json()
    #unique_task_id = body_create_response["task"]["task_id"]
    #2
    unique_task_id = response_create.json()["task"]["task_id"]
    #3
    updated_body = {"content": "Nakarm kota",
                    "user_id": "Alamakota_1",
                    "task_id": unique_task_id,
                    "is_done": True
                    }
    response_delete = requests.delete(url=ENDPOINT + "/delete-task/" + unique_task_id)
    assert response_delete.status_code == 200

    #4
    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 404
    msg = response.json()["detail"]
    assert msg == f"Task {unique_task_id} not found"

# def test_list_empty()
#1. list task for random user
#2. response body should be empty

def test_create_10_new_users():
    task_body = {"content": "random_task",
                 "user_id": "random_user",
                 "task_id": "01",
                 "is_done": True
                 }
    for i in range(1,10):
         response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200




# def test_list_empty()
#1. Create 10 tasks for users
#2. response body list should contain 10 tasks

