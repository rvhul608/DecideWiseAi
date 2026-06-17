import firebase_admin
from firebase_admin import credentials , auth
import os

cred = credentials.Certificate(os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH"))
firebase_admin.initialize_app(cred)


def verify_token(id_token:str) -> str:
    decoded = auth.verify_id_token(id_token)
    uid = decoded["uid"]
    return uid