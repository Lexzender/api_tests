from pydantic import BaseModel

class ExerciseSchema(BaseModel):
    """
        Описание структуры курса
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа полученного курса
    """
    exercise : list[ExerciseSchema]

class CreateExerciseResponseSchema(BaseModel):
    """
        Описание структуры ответа созданного курса
    """
    exercise: ExerciseSchema

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str