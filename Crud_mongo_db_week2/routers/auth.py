from fastapi import APIRouter, Depends, HTTPException, status
from beanie import PydanticObjectId
from datetime import datetime

from models.session_schema import Session
from utils.dependencies import Oauth2_scheme
import jwt
from config.settings import settings

router = APIRouter()


@router.post('/logout')
async def logout(token: str = Depends(Oauth2_scheme)):
    # Extract session_id out of the JWT bearer payload
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        session_id: str = payload.get("session_id")
        if not session_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid session token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    # Fetch the active session document from MongoDB
    session = await Session.get(PydanticObjectId(session_id))

    if not session or session.status != "active":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session is already invalid or expired")

    # Update and commit the status field changes directly to your MongoDB collection
    await session.set({
        "status": "inactive",
        "updated_at": datetime.now()
    })

    return {"detail": "Session successfully revoked in database. Logged out."}