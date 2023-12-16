from fastapi import APIRouter
from database.pydantic_models import KeyPair
from encryption_module.utils import generate_keys, convert_key_to_string

router = APIRouter(
    prefix="/items",
    tags = ['Items']
)

@router.get("/generatekeys", response_model = KeyPair)
def generatekeys():

    pubkey, privkey = generate_keys()
    pubkey = convert_key_to_string(pubkey)
    privkey = convert_key_to_string(privkey)
    
    return {
        "public_key": pubkey,
        "private_key": privkey
    }