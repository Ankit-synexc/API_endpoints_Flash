from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from models.user_schema import User
from models.session_schema import Session
from utils.auth import verify_pass, create_access_token

router = APIRouter()

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.find_one({"email": form_data.username})

    if not user or not verify_pass(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    session = await Session.find_one(Session.user_id == str(user.id), Session.status == 'active')
    if not session:
        session = Session(user_id=str(user.id), status='active')
        await session.insert()

    token = create_access_token(user_id=str(user.id), session_id=str(session.id))

    return {"access_token": token, "token_type": "bearer"}