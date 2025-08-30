from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import  PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_user, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("email", ["mail.ru", "gmail.com","example.com"])
def test_create_user(email: str,public_users_client: PublicUsersClient):

    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema(mail=fake.email(domain=email))
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Проверяем, что данные ответа совпадают с данными запроса
    assert_create_user_response(request, response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


def test_get_user_me(function_user: UserFixture,  # Используем фикстуру для создания пользователя
        authentication_client: AuthenticationClient,
                     private_users_client: PrivateUsersClient):
    # Запрос на логин (login_request -> request)
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    # Выполняем логин (login_response -> response)
    authentication_client.login_api(request)
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    validate_json_schema(response.json(), response_data.model_json_schema())
    assert_get_user_response(response_data, function_user.response)
