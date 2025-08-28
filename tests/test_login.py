from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()
    # Инициализируем API-клиент для авторизации
    authentication_client = get_authentication_client()
    #Создание нового юзера
    request = CreateUserRequestSchema()
    new_user = public_users_client.create_user(request)
    #Авторизация созданным юзером
    login_response = authentication_client.login_api(LoginRequestSchema(email=request.email, password=request.password))
    print(login_response.json())
    #Десериализовать JSON-ответ в LoginResponseSchema
    #Этот шаг нужен, чтобы преобразовать JSON-ответ в объект LoginResponseSchema, что упростит дальнейшие проверки.
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    #Проверить статус-код ответа (200)
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    #Проверить корректность тела ответа
    assert_login_response(login_response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())