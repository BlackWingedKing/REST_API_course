from werkzeug.security import safe_str_cmp # works on old python and others...
from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = { u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# user authentication function
def authenticate(username, password):
    """
    docstring
    """
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    # this function is unique to flask kwts
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
