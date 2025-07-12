import requests
response_get = requests.get("https://todo.pixegami.io")
print(response_get) #response [200]
print(response_get.status_code) #int
print(response_get.json()) #dict
print(response_get.json()["message"])

body = response_get.json()     # body:{message}
print(body["message"])



def test_can_call_api():
    response = requests.get("https://todo.pixegami.io")
    code = response.status_code
    expected = 200
    print (f"expected: {expected}, status_code: {code}")
    assert code == expected