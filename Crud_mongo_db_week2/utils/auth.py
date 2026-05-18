import bcrypt
import jwt
from datetime import datetime , timedelta , timezone
from config.settings import Settings

def hash_pass(password : str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

def verify_pass(plain_pass : str, hashed_pass : str):
    return bcrypt.checkpw(plain_pass.encode("utf-8"),hashed_pass.encode("utf-8"))

def create_access_token(user_id : str , session_id : str):
    payload = {
        "user_id" : user_id,
        "session_id" : session_id,
        "exp" : datetime.now(timezone.utc ) + timedelta(hours = 1)
    }
    return jwt.encode(payload, Settings.SECRET_KEY, algorithm =Settings.ALGORITHM )

