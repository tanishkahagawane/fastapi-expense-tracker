
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserRequestDto(BaseModel):
    username: str = Field(
        ..., min_length=3, max_length=50,
        description="The username"
    )
    email: EmailStr = Field(
        ..., description="The user's email address"
    )
    password: str = Field(
        ..., min_length=8, max_length=128,
        description="The user's password"
    )


class UserUpdateDto(BaseModel):
    username: str = Field(
        ..., min_length=3, max_length=50
    )
    email: EmailStr
    password: str = Field(
        ..., min_length=8, max_length=128
    )


class UserResponseDto(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# authentication schemas
class LoginRequest(BaseModel):
    email:str= Field(...,description="Email id of user")
    password:str=Field(...,description="Password of the user")

class LoginResponse(BaseModel):
    access_token:str
    user:UserResponseDto
