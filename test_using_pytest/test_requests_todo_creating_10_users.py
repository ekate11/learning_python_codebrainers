import requests

ENDPOINT = "https://todo.pixegami.io"

# def test_list_empty()
#1. Create 10 tasks for users
#2. response body list should contain 10 tasks

def test_create_10_tasks():
   
    task_body = {"content": "random_task",
                 "user_id": "random_user",
                 "task_id": "01",
                 "is_done": True
                 }
    
    for response_create in range(10):
         response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
         response_body = (response_create.json()["task"]["task_id"])
         #response_body_list = []
         #response_body_list.append(response_body)
    
    response_body_list = []  # Inicjalizacja pustej listy
    i = 1       # Inicjalizacja zmiennej iteracyjnej
    while i <= 10:  # Warunek pętli: iteruj 5 razy
        response_body = (response_create.json()["task"]["task_id"]) # Pobierz task
        response_body_list.append(response_body)  # Dodaj task do listy
        i += 1  # Zwiększ iterator
    print(response_body_list)
        
    assert response_create.status_code == 200
    
    response_get = requests.get(url=ENDPOINT + "/list-tasks/" + "radom_user")

    assert response_get.status_code == 200
    
