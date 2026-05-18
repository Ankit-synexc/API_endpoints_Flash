from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from beanie import PydanticObjectId
from config.settings import settings
from models.session_schema import Session
from models.user_schema import User

Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_active_user(token: str = Depends(Oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        session_id: str = payload.get("session_id")

        if user_id is None or session_id is None:
            raise credentials_exception

        pydantic_user_id = PydanticObjectId(user_id)
        pydantic_session_id = PydanticObjectId(session_id)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ValueError, Exception):
        raise credentials_exception

    session = await Session.get(pydantic_session_id)

    if not session or session.status != "active":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session has been revoked or is invalid"
        )

    user = await User.get(pydantic_user_id)
    if not user:
        raise credentials_exception

    return user