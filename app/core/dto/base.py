from pydantic import BaseModel, Extra


class Base(BaseModel):
    class Config:
        use_enum_values = True
        extra = Extra.forbid
        frozen = False
        from_attributes = True

