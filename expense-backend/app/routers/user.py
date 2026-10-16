
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password

from app.core.db import get_db
from app.models.user import User
from app.schemas.user import UserRequestDto, UserUpdateDto, UserResponseDto
from app.schemas.api_response import ApiResponse


user_router = APIRouter(prefix="/users", tags=["Users"])


# Create user
@user_router.post("/", response_model=ApiResponse,
                  status_code=status.HTTP_201_CREATED)
def create_user(
    user_request: UserRequestDto,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        (User.username == user_request.username) |
        (User.email == str(user_request.email))
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )

    new_user = User(
    username=user_request.username,
    email=str(user_request.email),
    password=hash_password(user_request.password)
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return ApiResponse(
        status="success",
        message="User created successfully",
        data={"user": UserResponseDto.model_validate(new_user)}
    )


# Get all users
@user_router.get("/", response_model=ApiResponse)
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return ApiResponse(
        status="success",
        message="Users retrieved successfully",
        data={
            "users": [
                UserResponseDto.model_validate(user)
                for user in users
            ]
        }
    )


# Get user by ID
@user_router.get("/{user_id}", response_model=ApiResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return ApiResponse(
        status="success",
        message="User retrieved successfully",
        data={"user": UserResponseDto.model_validate(user)}
    )


# Update user by ID
@user_router.put("/{user_id}", response_model=ApiResponse)
def update_user(
    user_id: int,
    user_request: UserUpdateDto,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    duplicate = db.query(User).filter(
        User.id != user_id,
        (User.username == user_request.username) |
        (User.email == str(user_request.email))
    ).first()

    if duplicate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )

    user.username = user_request.username
    user.email = str(user_request.email)
    user.password = hash_password(user_request.password)

    db.commit()
    db.refresh(user)

    return ApiResponse(
        status="success",
        message="User updated successfully",
        data={"user": UserResponseDto.model_validate(user)}
    )


# Delete user by ID
@user_router.delete("/{user_id}", response_model=ApiResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return ApiResponse(
        status="success",
        message="User deleted successfully",
        data={"user_id": user_id}
    )
