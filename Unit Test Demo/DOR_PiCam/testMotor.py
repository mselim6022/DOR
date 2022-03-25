import RPi.GPIO as GPIO
import time
import pyrebase

config = {
    'apiKey': "AIzaSyAlEeYWPWcWMb54phvOCinxNgynm1vzAzo",
    'authDomain': "sysc3010-dor.firebaseapp.com",
    'databaseURL': "https://sysc3010-dor-default-rtdb.firebaseio.com/",
    'storageBucket': "sysc3010-dor.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
instructions = db.child("Instructions").get()
range_amount = 0
for instruction in instructions.each():
        print("Pulled data from database:\nPulled value:\n" + str(instruction.val()))
        range_amount = range_amount + 512


GPIO.setmode(GPIO.BOARD)
control_pins = [15,13,16,18]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
for i in range(range_amount):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()
