import pyrebase

config = {
    'apiKey': "AIzaSyAlEeYWPWcWMb54phvOCinxNgynm1vzAzo",
    'authDomain': "sysc3010-dor.firebaseapp.com",
    'databaseURL': "https://sysc3010-dor-default-rtdb.firebaseio.com/",
    'storageBucket': "sysc3010-dor.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

data={"Action": "Open", "Device": "DOR1", "Time": "01/11/2001, 12:30:00"}
db.child("Instructions").child(0).set(data)
data={"Action": "Close", "Device": "DOR1", "Time": "03/11/2022, 22:22:22"}
db.child("Instructions").child(1).set(data)
data={"Action": "Open", "Device": "DOR2", "Time": "03/12/2022, 10:30:00"}
db.child("Instructions").child(2).set(data)



