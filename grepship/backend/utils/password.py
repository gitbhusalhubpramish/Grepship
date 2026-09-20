def check_password_strength(password): # function 

    if len(password) < 8:
        return False, "password must be at least 8 characters"

    if len(password) > 100:
        return False, "password must be under 100 characters"

    if not any(c.isupper() for c in password):
        return False, "password must contain an uppercase letter"

    if not any(c.islower() for c in password):
        return False, "password must contain a lowercase letter"

    if not any(c.isdigit() for c in password):
        return False, "password must contain a number"

    return True, "" # Return empty if none is valid

    # CREATED FOR PASSWORD VALIDATION. 
