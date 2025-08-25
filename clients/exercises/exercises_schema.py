from pydantic import BaseModel, Field

from tools.fakers import fake


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
    title: str =  Field(default_factory=fake.sentence)
    courseId: str = Field(default_factory=fake.uuid4)
    max_score : int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimatedTime: str =Field(default_factory=fake.estimated_time)


class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str =  Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimatedTime: str = Field(default_factory=fake.estimated_time)