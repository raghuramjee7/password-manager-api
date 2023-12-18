from fastapi import APIRouter, Depends, HTTPException, status
from database.connect import get_db
from database.model import User
from utils.encryption_util import encrypt_password, decrypt_password
from database.pydantic_models import ItemIn, ItemOut, ItemDelete
from sqlalchemy.orm import Session
from utils.auth_util import validate_user
from database import model

router = APIRouter(
    prefix="/items",
    tags = ['Items']
)

@router.get("/", response_model=ItemOut)
async def search(search_item: str, db: Session = Depends(get_db), current_user: User = Depends(validate_user)):
    
    search_item = search_item.lower()
    result = db.query(model.Item).filter(model.Item.owner_id == current_user.id, model.Item.site.contains(search_item)).first()

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item = ItemOut(
        site = result.site,
        username = result.username,
        password = result.password
    )

    return item


@router.post("", response_model = ItemOut)
async def create_item(item: ItemIn, db = Depends(get_db), current_user: User = Depends(validate_user)):

    url = item.url.host
    url_query = db.query(model.Item).filter(model.Item.site == url, model.Item.owner_id == current_user.id).first()

    if url_query is not None:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    new_item = model.Item(
        
        site = item.url.host,
        username = item.username,
        password = item.password,
        owner_id = current_user.id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

@router.put("")
async def update_item(item: ItemIn, db = Depends(get_db), current_user: User = Depends(validate_user)):
    url = item.url.host
    url_query = db.query(model.Item).filter(model.Item.site == url, model.Item.owner_id == current_user.id)

    if url_query.first() is None:
        raise HTTPException(status_code=400, detail="Item does not exists")
    
    url_query.update(
        {
            "username": item.username,
            "password": item.password
        }
    )

    db.commit()

    return {"message": "Item updated"}

@router.delete("", status_code = status.HTTP_204_NO_CONTENT)
async def delete_item(item: ItemDelete, db = Depends(get_db), current_user: User = Depends(validate_user)):
    url = item.url.host
    url_query = db.query(model.Item).filter(model.Item.site == url, model.Item.owner_id == current_user.id)
    if url_query.first() is None:
        raise HTTPException(status_code=400, detail="Item does not exists")
    
    url_query.delete(synchronize_session=False)
    db.commit()