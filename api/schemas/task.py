from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")


class TaskCreate(TaskBase):
    pass

    class Config:
        orm_mode = True

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
