import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExercisesRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
        function_course: CourseFixture,
        function_user: UserFixture,
) -> ExerciseFixture:
    request = CreateExercisesRequestSchema(
        courseId=function_course.course.id
    )
    response = courses_client.create_course(request)
    return ExerciseFixture(request=request, response=response)