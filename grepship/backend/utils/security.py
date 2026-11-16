# from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

def hash_password(password: str) -> str:
    
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=12)).decode()


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash)
