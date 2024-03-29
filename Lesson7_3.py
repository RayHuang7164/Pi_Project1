import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#產生KEY  https://console.firebase.google.com/project/raspberry-1129a/settings/serviceaccounts/adminsdk
#參考文件 https://firebase.google.com/docs/database/admin/start?hl=zh-tw&authuser=0#python

cred = credentials.Certificate("raspberry-1129a-firebase-adminsdk-75033-ae5ba56285.json")
#firebase_admin.initialize_app(cred)

# Database 位置 https://console.firebase.google.com/project/raspberry-1129a/database/raspberry-1129a-default-rtdb/data
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberry-1129a-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/mfrc')

# 更新雲端資料庫資料 
# 參考 https://firebase.google.com/docs/database/admin/save-data?hl=zh-tw&authuser=0
ref.update({
    'id': 'Hello! Raspberry'
})