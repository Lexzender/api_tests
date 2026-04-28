import pytest
from pydantic import BaseModel

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    """
    Определяем вспомогательный класс FileFixture
    Этот класс представляет объект, содержащий:

    request — данные запроса на загрузку файла (CreateFileRequestSchema).
    response — ответ от API после успешного создания файла (CreateFileResponseSchema).
    Использование BaseModel из pydantic позволяет работать с объектом более удобно и с проверкой типов.
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:

    """
    Эта фикстура автоматически создает тестовый файл перед каждым тестом и возвращает информацию о нем:

    Создается объект request типа CreateFileRequestSchema, в котором указывается путь к тестовому файлу (./testdata/files/image.png).
    Затем files_client.create_file(request) отправляет запрос в API, загружая файл.
    После успешного создания файла возвращается объект FileFixture, содержащий данные запроса и ответа API.
    Таким образом, при вызове function_file в тестах уже будет готовый загруженный файл, который можно использовать для дальнейших проверок.
    """
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
