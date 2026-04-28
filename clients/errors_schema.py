from typing import Any

from pydantic import BaseModel, Field, ConfigDict

"""
Почему мы создали отдельный файл errors_schema.py?
Ошибки валидации имеют единый формат во всех эндпоинтах API. Вместо того чтобы дублировать код и писать отдельные модели для каждого эндпоинта, мы создали универсальную схему обработки ошибок, которая позволит:

Избежать дублирования кода.
Гибко работать с любыми эндпоинтами, возвращающими ошибки валидации.
"""



class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")

class InternalErrorResponseSchema(BaseModel):
    """
    Модель для описания внутренней ошибки.
    """

    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")
