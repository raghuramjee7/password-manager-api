from pydantic import BaseModel, HttpUrl, UrlConstraints
from typing import Annotated, Optional

from pydantic_core import Url

class KeyPair(BaseModel):
    public_key: str
    private_key: str

class UserIn(BaseModel):
    username: str
    password: str
    
class UserOut(BaseModel):
    username: str
    public_key: str
    created_at: str

class ItemDelete(BaseModel):
    url: HttpUrl = Annotated[
                Url,
                UrlConstraints(
                    max_length=2083, allowed_schemes=["http", "https"]
                ),
            ]

class ItemIn(BaseModel):
    url: HttpUrl = Annotated[
                Url,
                UrlConstraints(
                    max_length=2083, allowed_schemes=["http", "https"]
                ),
            ]
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