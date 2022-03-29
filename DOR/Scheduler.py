import pyrebase
import datetime

config = {
    'apiKey': "AIzaSyAlEeYWPWcWMb54phvOCinxNgynm1vzAzo",
    'authDomain': "sysc3010-dor.firebaseapp.com",
    'databaseURL': "https://sysc3010-dor-default-rtdb.firebaseio.com/",
    'storageBucket': "sysc3010-dor.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

instructions = db.child("Instruction").get()


for instruction in instructions.each():
     print(instruction.val())