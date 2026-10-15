# all the apis of authentication
from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")

@auth_router.post("/login")
def login():
    print("login api called")
    return{
        "message":"login api called"
    }

@auth_router.post("/register")
def register():
    print("register api called")
    return{
        "message":"register api called"
    }