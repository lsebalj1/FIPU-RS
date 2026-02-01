from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional

class UserProfile(BaseModel):
    id : int = Field(gt=0)
    username : str = Field(min_length=3, max_length=20)
    full_name : Optional[str] = Field(min_length=3, max_length=50)
    bio : str = Field(min_length=20, max_length=140)
    friends : list[str]
    rank : Literal["beginner", "intermediate", "advanced"]
    email : EmailStr 


class UserProfileInput(BaseModel):
    username : str = Field(min_length=3, max_length=20)
    email : str
    full_name : Optional[str] = Field(min_length=3, max_length=50)
    bio : str = Field(min_length=20, max_length=140)
    email : EmailStr    
    