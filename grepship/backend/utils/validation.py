import re

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def get_str(data, key, strip=True):

    value = data.get(key)
    if not isinstance(value, str):
        return ""
    return value.strip() if strip else value

def valid_username(username):
    return bool(USERNAME_RE.match(username))

def valid_email(email):
    return bool(EMAIL_RE.match(email))
