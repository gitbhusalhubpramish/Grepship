from utils.redis import redis_client
from models.user import find_user_by_email_or_username

def auth_user_by_session(session):
	user = redis_client.get(f"session{session}")
	user = find_user_by_email_or_username(username=user)
	return user
