import httpx

from faker import Faker
fake = Faker()
BASE_URL = "http://localhost:8000/"
CREATE_USER = "api/v1/users"
LOGIN = 'api/v1/authentication/login'
GET_ME = "api/v1/users/me"
PATCH_USER_ID = "api/v1/users/"
GET_USER_ID = "api/v1/users/"
DELETE_USER_ID = "api/v1/users/"
user = {
  "email": fake.email(),
  "password": "string123",
  "lastName": "Kost",
  "firstName": "Alex",
  "middleName": "Pavl"
}

response = httpx.post(BASE_URL+CREATE_USER, json=user)
print(response.status_code)
print(response.json())
USER_ID = response.json()["user"]["id"]
print("сохраненный id юзера:",USER_ID)
"""
Отправит POST-запрос на эндпоинт /api/v1/authentication/login с необходимыми учетными данными и получит accessToken из ответа.
"""
data= {
    "email": "test_user@example.com",
    "password": "string123"
}

response = httpx.post(BASE_URL+LOGIN, json=data)
print(response.status_code)
print(response.json())

accessToken = response.json()["token"]["accessToken"]
print("Токен доступа:", accessToken)

"""
Используя полученный accessToken, выполнит GET-запрос к эндпоинту /api/v1/users/me.
"""
headers = {"Authorization": f"Bearer {accessToken}"}
response = httpx.get(BASE_URL + GET_ME, headers=headers)
print(response.status_code)
print(response.json())

"""
После авторизации выполнить PATCH запрос для обновления пользователя на эндпоинт /api/v1/users/{user_id}. В теле запроса необходимо передать JSON в следующем формате: 
"""
updated_user_body = {
  "email": fake.email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
response = httpx.patch(BASE_URL + PATCH_USER_ID + USER_ID,json=updated_user_body,headers=headers)
print(response.status_code)
print("Модифицированный юзер:", response.json())

response = httpx.get(BASE_URL + GET_USER_ID + USER_ID,headers=headers)
print(response.status_code)
print(response.json())

response = httpx.delete(BASE_URL + DELETE_USER_ID + USER_ID,headers=headers)
print(response.status_code)

response = httpx.get(BASE_URL + GET_USER_ID + USER_ID,headers=headers)
print(response.status_code)
print(response.json())