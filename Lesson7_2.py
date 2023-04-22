import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("raspberry-1129a-firebase-adminsdk-75033-ae5ba56285.json")
firebase_admin.initialize_app(cred)