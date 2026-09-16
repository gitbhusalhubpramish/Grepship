from extensions import mongo
from bson import ObjectId
from datetime import datetime, timezone
from bson.errors import InvalidId 

def create_user(username, email, password_hash, profile_pic=None):
    result = mongo.db.users.insert_one({               # Creating a result dictionary thing that store the user data  if available 
        'username': username, # Username storing of user 
        'email': email, # email storing of user
        'password_hash': password_hash, # hashed password saving 
        'profile_pic': profile_pic, # profile pic if needed
        'created_at': datetime.now(timezone.utc), # Takes the time 
        'friends': [], # list all the friend at the site
    })
    return str(result.inserted_id) # returns result of user entered 

def find_user_by_email(email): # function created to find the user id by using email entered by user
    return mongo.db.users.find_one({"email": email}) # Returns the result if have

def  find_user_by_username(username): # Function created to find the user id by username existence
    return mongo.db.users.find_one({'username': username})  # Returns all the existences usernames from the database

def find_user_by_id(user_id): # Function created to find the user id by using user id entered
    try: # Try to find the user with this id
        return mongo.db.users.find_one({'_id': ObjectId(user_id)})
    except InvalidId: # To raise the error if not existed
        return None 

# This is a file created to work with user input.
