from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )


# Что нам это дает?
#
#     Если захотим заменить jsonschema на другую библиотеку (например, pydantic или fastjsonschema), просто обновим код в одном месте.
#     Можно легко добавить логирование или интеграцию с Allure (например, оборачивать в allure.step).
#     Все автотесты в будущем смогут использовать единый интерфейс валидации, а значит, код станет чище и проще в поддержке.
