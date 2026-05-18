from fastapi import Depends ,HTTPException , status
from fastapi.security import OAuth2PasswordBearer
import jwt
from beanie import PydanticObjectId
from config.settings import Settings
from models.session_schema import  Session
from models.user_schema import User

Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_active_user(token: str = Depends(Oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token , Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM])
        user_id: str = payload.get("sub")
        session_id : str = payload.get("session_id")

        if user_id is None or session_id is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401 , detail="Expired. Please log in again")
    except jwt.InvalidTokenError:
            raise credentials_exception
    session = await Session.get(PydanticObjectId(session_id))
    if not session or not session.status != "active":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "session has been revoked"
            )

    user = await User.get(PydanticObjectId(user_id))
    if not user:
        raise credentials_exception
    return user




