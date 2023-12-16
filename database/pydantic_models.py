from pydantic import BaseModel
from typing import Optional

class KeyPair(BaseModel):
    public_key: str
    private_key: str

class UserIn(BaseModel):
    username: str
    password: str
    public_key: str

class UserOut(BaseModel):
    username: str
    public_key: str
    created_at: str

class ItemIn(BaseModel):
    site: str
    username: str
    password: str

class ItemOut(BaseModel):
    site: str
    username: str
    password: str

class Search(BaseModel):
    site: str
    private_key: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None