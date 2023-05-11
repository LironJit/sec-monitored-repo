# hi


import jwt

token = 'your_jwt_token'
decoded_token = jwt.decode(token, verify=False)
