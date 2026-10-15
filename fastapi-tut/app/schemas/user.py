from pydantic import BaseModel,Field

class UserDto(BaseModel):
    firstName:str=Field(...,max_length=10,min_length=2)
    lastName:str
    city:str
    age:int
    active:bool=True
