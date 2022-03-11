import socket
import pyrebase

HOST = "127.0.0.1"
PORT =  6969
config = {
    'apiKey': "AIzaSyAlEeYWPWcWMb54phvOCinxNgynm1vzAzo",
    'authDomain': "sysc3010-dor.firebaseapp.com",
    'databaseURL': "https://sysc3010-dor-default-rtdb.firebaseio.com/",
    'storageBucket': "sysc3010-dor.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#Setting up the test/Sending messages to database
data={"Action": "Open", "Device": "DOR1", "Time": "01/11/2001, 12:30:00"}
db.child("Instructions").child(0).set(data)
data={"Action": "Close", "Device": "DOR1", "Time": "03/11/2022, 22:22:22"}
db.child("Instructions").child(1).set(data)
data={"Action": "Open", "Device": "DOR2", "Time": "03/12/2022, 10:30:00"}
db.child("Instructions").child(2).set(data)

#retreiving database
instructions = db.child("Instructions").get()

#expected values for tests
expected = ["{'Action': 'Open', 'Device': 'DOR1', 'Time': '01/11/2001, 12:30:00'}",
                "{'Action': 'Close', 'Device': 'DOR1', 'Time': '03/11/2022, 22:22:22'}",
                "{'Action': 'Open', 'Device': 'DOR2', 'Time': '03/12/2022, 10:30:00'}"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    i = 0
    passesDB = 0
    #Tests if messages were properly sent to database
    for instruction in instructions.each():
        print("Pulled data from database:\nPulled value:\n" + str(instruction.val()) + "\nExpected:\n" + expected[i])
        if (str(instruction.val())==expected[i]):
            print("Test Passed\n")
            passesDB += 1
        i += 1
        
    print("Tests Passed: " + f"{passesDB}/3" + "\n\n")

    j = 0
    passesTCP = 0

    #Tests TCP connection with DOR device
    for instruction in instructions.each():
        s.sendall(bytes(str(instruction.val()),'utf-8'))
        data = s.recv(1024)
        print("Received response from DOR:\nReceived response:\n" + str(instruction.val()) + "\nExpected:\n" + expected[j])
        if (str(instruction.val())==expected[j]):
            print("Test Passed\n")
            passesTCP += 1
        
        j += 1
        
    print("Tests Passed: " + f"{passesTCP}/3" + "\n\n")
    
