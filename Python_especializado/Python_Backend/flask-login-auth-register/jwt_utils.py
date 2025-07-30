from jwt import JWT
import datetime
from dotenv import load_dotenv
import os

#Cargar las variables de entorno
load_dotenv()

secret_key = os.getenv('SECRET_KEY')
jwt_expiration = os.getenv('JWT_EXPIRATION')

jwt = JWT()

#Generar el token
def generate_token(user_id):
  payload = {
    'sub': user_id,
    'exp': datetime.datetime.now() + datetime.timedelta(seconds=int(jwt_expiration)),
    'iat': datetime.datetime.now()
  }
  return jwt.encode(payload, secret_key, alg="HS256")

#verificar el token

def verify_token(token):
  try:
    payload = jwt.decode(token, secret_key, alg=['HS256'])
    return payload['sub']
  except jwt.ExpiredSignatureError:
    return "Token expirado"
  except jwt.InvalidTokenError:
    return "Token"