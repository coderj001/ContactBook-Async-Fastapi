from pydantic import BaseModel


class ContactBookSchema(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "sample_name",
                "email": "sample@name.com",
            }
        }
