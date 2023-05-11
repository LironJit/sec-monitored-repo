# /python.jwt.security.unverified-jwt-decode.unverified-jwt-decode.json
import jwt

token = 'your_jwt_token'
decoded_token = jwt.decode(token, verify=False)
