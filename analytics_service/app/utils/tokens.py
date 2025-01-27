import os
import jwt
import logging
from datetime import datetime, timedelta

from enums.env import EnvironmentVariables


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_token(payload, expiration_hours=360):
    logger.error(f"Generating the token")
    payload["exp"] = datetime.today() + timedelta(hours=expiration_hours)
    return jwt.encode(payload, EnvironmentVariables.JWT_SECRET.value, algorithm="HS256")


def decode_token(token: str):
    try:
        logger.info(f"Trying to decode the token")
        return jwt.decode(
            token,
            EnvironmentVariables.JWT_SECRET.value,
            verify=True,
            algorithms=["HS256"],
        )
    except Exception as e:
        logger.error(f"Failed to decode the token with error: {e}")
        return None


def validate_token(token: str):
    decoded_token = decode_token(token)
    if (
        not decoded_token
        or decoded_token.get("exp") <= datetime.today().timestamp() + 10 * 60
    ):
        logger.info("Token is expired or failed to decode. Refresh it.")
        return None
    return decoded_token.get("username")
