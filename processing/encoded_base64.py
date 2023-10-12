import pybase64 as base64
import credentials

def encoded():
  credential = f'{credentials.key}:{credentials.secret_key}'
  credential_bytes = credential.encode('utf-8')
  encoded = base64.b64encode(credential_bytes)
  return encoded.decode('utf-8')