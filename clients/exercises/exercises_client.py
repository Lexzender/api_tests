from httpx import Response
from clients.exercises.exercises_schema import GetExercisesResponseSchema, ExerciseResponseSchema, GetExercisesQuerySchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client



class ExercisesClient(APIClient):
    """
        Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
                Метод получения списка упражнений.

                :param query: Словарь с courseId .
                :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises",  params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
                Метод получения упражнения.

                :param exercise_id: Идентификатор упражнения
                :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description,
        estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description,
        estimatedTime
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, query: GetExercisesQuerySchema)-> GetExercisesResponseSchema:
        response = self.get_exercise_api(query)
        return  response.json()

    def create_exercises(self,request:CreateExerciseRequestSchema) -> ExerciseResponseSchema:
        response = self.create_exercises_api(request)
        return ExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
