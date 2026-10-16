from pydantic import BaseModel,Field
from typing import Optional


class ApiResponse(BaseModel):
    status: str
    message:str
    data: Optional[dict] = None
    