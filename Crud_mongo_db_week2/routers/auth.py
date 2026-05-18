from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from beanie import PydanticObjectId
from datetime import datetime
import jwt

from models.session_schema import Session
from utils.dependencies import Oauth2_scheme
from utils.auth import verify_pass, create_access_token
from services.user_services import db_get_user_by_email
from config.settings import settings

router = APIRouter()

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db_get_user_by_email(form_data.username)
    if not user or not verify_pass(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    session = await Session.find_one(
        Session.user_id == str(user.id),
        Session.status == "active"
    )

    if session:
        await session.set({"updated_at": datetime.now()})
    else:
        session = Session(
            user_id=str(user.id),
            status="active",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        await session.insert()

    token = create_access_token(user_id=user.id, session_id=session.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post('/logout')
async def logout(token: str = Depends(Oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        session_id: str = payload.get("session_id")
        if not session_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid session token")
        pydantic_session_id = PydanticObjectId(session_id)
    except (jwt.PyJWTError, ValueError, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    session = await Session.get(pydantic_session_id)

    if not session or session.status != "active":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session is already invalid or expired")

    await session.set({
        "status": "inactive",
        "updated_at": datetime.now()
    })

    return {"detail": "Session successfully revoked in database. Logged out."}