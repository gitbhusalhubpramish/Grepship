import re

#   Username verification helper
USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,20}$")

#  Same as USERNAME_RE but for email
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def get_str(data, key, strip=True):

    value = data.get(key)

    if not isinstance(value, str):
        return ""
   
    return value.strip() if strip else value

def valid_username(username):
    return bool(USERNAME_RE.match(username)) # Is username valid to move on 

def valid_email(email):
    return bool(EMAIL_RE.match(email)) # Is email valid to move on 

# For username and email validation