from fastapi import APIRouter, HTTPException, status
from models import UserProfile, UserProfileInput
import uuid

router = APIRouter()

users = []

@router.get("/users", response_model = list[UserProfile])
def get_users():
    return users

@router.get("/users/{id}", response_model = UserProfile)
def get_user_by_id(id : int):
    for user in users:
        if user["id"] == id:
            return user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opis greške")

@router.get("/users/{username}", response_model = UserProfile)
def get_users(username : str):
    for user in users:
        if user["username"] == username:
            return user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opis greške")

@router.post("/users", response_model = UserProfile)
def new_user(userProfileInput : UserProfileInput):
    
    new_id = str(uuid.uuid4())
    
    new_friends : list[str] = [] 
    
    new_rank = "beginner"
    
    new_user_profile = UserProfile(
        id = new_id,
        username = userProfileInput.username,
        full_name = userProfileInput.full_name,
        bio = userProfileInput.bio, 
        friends = new_friends,
        rank = new_rank,
        email = userProfileInput.email
    )
    
    users.append(new_user_profile)
    
'''
@router.post("/users/friend", response_model = UserProfile)
def new_friend(username : str):
    for user in users:
        if user["username"] == username:
            return user
'''

                
    