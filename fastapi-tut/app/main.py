from fastapi import FastAPI,Depends,status,HTTPException
from .schemas.api  import ApiResponse
from .schemas.user import UserDto
from .routers.auth import auth_router
from .routers.users import user_router


app =  FastAPI(
    title="fastapi",
    description="BE using fastapi",
    version="1.0"
)

@app.get("/")
def root():
    print("This is root api")

    return{
        "message":"BE server is Working "
    }


#######################################
@app.get("/home",response_model=ApiResponse)
def home():
    response =  ApiResponse( message = "Hey",success=True,status="OK")
    return  response

@app.get("/get-users")
def get_users():
    print("getting all users")

    return [
        "aniket",
        "sachin",
        "rahul"
    ]
############################
# Path operations
#GET , POST , PUT, DELETE
@app.get("/users")
def get_users():
    print("getting all users")

    return [
        "aniket",
        "sachin",
        "rahul"
    ]

@app.post("/users")
def create_users():
    print("creating user")

    return  ApiResponse(
        message="create new user successfully!",
        status="OK",
        success=True
    )

#####################################
#Path parameters
#1. URL path variables

@app.put("/users/{user_id}/name/{user_name}")
def update_user(user_id:int,user_name:str):
    print("user update")
    print("user name",user_name)
    print("user id",user_id)
    return  ApiResponse(
            message="updated user successfully!",
            status="OK",
            success=True
        )

#2. query parameters - used for search

@app.get("/users/search")
def search_user(firstName:str="",lastName:str="",city:str=""):
    print(firstName,lastName,city)
    print("searching user")
    return {
        "data":[],
        "success":True
    }

############################
#request body

@app.post("/requsers")
def create_user(user:UserDto):
    print("firstname ",user.firstName)
    print("lastname ",user.lastName)
    return {
        "message":"user created successfully",
        "user":user

    }

#############################
#Dependency Injection (DI) 
#in FastAPI is a built-in mechanism that allows you to extract, share, and automatically inject reusable logic into your API endpoints

def get_token():
    print("getting token ...")
    return "toke_amdncbjkbchesh"


@app.post("/requserstoken",status_code=status.HTTP_201_CREATED)
def create_usert(user:UserDto,token=Depends(get_token)):

    if user.firstName == "abc":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This user is not allowed try again!"
        )
    print("firstname ",user.firstName)
    print("lastname ",user.lastName)
    return {
        "message":"user created successfully",
        "user":user,
        "token":token
    }

######################
#router

app.include_router(auth_router)
app.include_router(user_router)
