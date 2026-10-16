# functiosn that helps uset to perform jwt operations like encoding and decoding token


from datetime import datetime,timedelta,timezone
from jose import jwt 
from fastapi import HTTPException,status


SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#create access_token
def create_access_token(data : dict, expire_dalta:timedelta | None =  None):
    to_encode = data.copy()

    if expire_dalta:
        expire = datetime.now(timezone.utc) + expire_dalta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp":expire
    })

    encoded_token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_token

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        print("Invalid token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token !!"
        )


# refresh token create


if __name__=="__main__":
    print("This is main module",__name__)
    token=create_access_token({"name":"abc"})

    payload=verify_access_token(token)
    print("token verifies successfully")
    print(payload)
    print(token)


