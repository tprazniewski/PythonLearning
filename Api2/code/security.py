from user import User # from user file import User class

# users = [
#     {
#         'id': 1,
#         'user': 'tom',
#         'password': 'abcd'
#     }
# ]

users = [
    User(1, 'bob', 'abcd')
]

# username_mapping = {
#     'tom': {
#         'id': 1,
#         'user': 'tom',
#         'password': 'abcd'
#     } 
# }

username_mapping = { u.user: u for u in users} # set comprehension. it binding values

# userid_mapping = {
#     1: {
#         'tom': {
#         'id': 1,
#         'user': 'tom',
#         'password': 'abcd'
#         } 
#     }
# }

userid_mapping = { u.id: u for u in users}


def authenticate(user, password):
    user =username_mapping.get(user)
    if user and user.password == password:
        return user

def identity(payload): # payload content of JWT token
    user_id = payload['identity'] #extract user id from the payload
    return userid_mapping.get(user_id, None)