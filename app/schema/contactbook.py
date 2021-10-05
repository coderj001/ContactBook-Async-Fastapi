from pydantic import BaseModel
from typing import Optional


class ContactBookResSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "sample_name",
                "email": "sample@name.com",
            }
        }


class ContactBookSchema(BaseModel):
    name: str
    email: str

    class Config:
        schema_extra = {
            "example": {
                "name": "sample_name",
                "email": "sample@name.com",
            }
        }


class ContactBookUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "sample_name",
                "email": "sample@name.com",
            }
        }
