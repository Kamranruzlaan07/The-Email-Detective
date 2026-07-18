from pydantic import BaseModel


class EmailHeaderRequest(BaseModel):
    header: str