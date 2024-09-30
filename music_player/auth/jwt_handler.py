import os
import time
from typing import Dict
import jwt

# Define your secret key here or load it from an environment variable
secret_key = os.getenv("SECRET_KEY", "your-secret-key")

def token_response(token: str):
    return {"access_token": token}

def sign_jwt(user_id: str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {"user_id": user_id, "expires": time.time() + 2400}
    return token_response(jwt.encode(payload, secret_key, algorithm="HS256"))

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token.encode(), secret_key, algorithms=["HS256"])
        return decoded_token if decoded_token["expires"] >= time.time() else {}
    except jwt.ExpiredSignatureError:
        return {}  # Token has expired
    except jwt.InvalidTokenError:
        return {} 
