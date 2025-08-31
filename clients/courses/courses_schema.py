from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema
from pydantic import BaseModel, Field

from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema
    estimatedTime: str
    createdByUser: UserSchema  # Вложенная структура пользователя

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    title: str = Field(default_factory=fake.sentence)
    maxScore: int = Field(alias="maxScore", default_factory=fake.max_score)
    minScore: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimatedTime: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    previewFileId: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    createdByUserId: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimatedTime: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
