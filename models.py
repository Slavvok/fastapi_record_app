from pydantic import BaseModel


class Record(BaseModel):
    id: int | None
    data: str
