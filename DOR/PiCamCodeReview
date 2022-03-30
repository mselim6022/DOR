#This code is supposed to check the status of our door
#It prompts the user to take a reference image first
#It will take this image to compare with a new picture to check the status of the door
#We put white space as a reference to compare whether the door is open or not
#If the threshold of the reference image and the new image is greater than 10, the door status has changed
from helper_functions import camera, computer_vision,sensehat
from time import sleep
import cv2
import numpy as np


def main():
    door_opened = False
    white = (200, 200, 200)
    percentWhiteBG = 0
    percentWhiteIMG = 0
    camera_i = camera.get_camera()
    sense = sensehat.get_sensehat()
    while True:
        option = input("Enter \'1\' if a reference image is saved in data/images/reference.png\n" +
        "Enter \'2\' to take the reference image\n")
        if(int(option) == 1):
            take_reference_image = False
        elif(int(option) == 2):
            take_reference_image = True
        else:
            continue
        if (take_reference_image):
            print("Get out of the scene!\n" +
            "Reference image will be taken in 5 seconds...")
            for i in range(5):
                sleep(1)
                print(5-i)
                
            preview = False
            countdown=0
            camera.capture_image(camera_i,"data/images/reference.jpg", countdown_time=countdown, preview=preview)
            print("Background image taken!\n")
            take_reference_image = False
            percentWhiteBG = computer_vision.percentage_color("data/images/reference.jpg", 55, white)
        while (not(take_reference_image)):
            optionArm = input("Would you like to arm the system? y/n\n")
            if (optionArm == "y"):
                arm_system = True
            elif(optionArm == "n"):
                arm_system = False
            else:
                continue
                
            if (arm_system):
                interval = int(input("Enter the interval between test images in seconds:\n"))
                t1 = int(input("Enter the threshold t1:\n"))
                
                print("Monitoring will begin in %d seconds..." % interval)
                for i in range(interval):
                    sleep(1)
                    print(interval - i)
                
                print("Monitoring has begun!")
                
                count = 0
                while True:
                    camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval)
                    percentWhiteIMG = computer_vision.percentage_color("data/images/image%s.jpg" % count, t1, white)
                    if (not door_opened):
                        if ((percentWhiteIMG - percentWhiteBG) > 10):
                            print("The Door is Open!")
                            door_opened = True
                            sensehat.alarm(sense,interval) 
                        else:
                            print("The door is still Closed") 
                        count += 1
                    elif(door_opened):
                        if ((percentWhiteIMG - percentWhiteBG) < 10):
                            print("The Door is Closed!")
                            door_opened = False
                            sensehat.alarm(sense,interval) 
                        else:
                            print("The door is still Opened") 
                        count += 1
            else:
              return

if __name__ == "__main__":
    main()
    
#./PiCam.py:1:53: E231 missing whitespace after ','
#./PiCam.py:3:1: F401 'cv2' imported but unused
#./PiCam.py:4:1: F401 'numpy as np' imported but unused
#./PiCam.py:15:80: E501 line too long (99 > 79 characters)
#./PiCam.py:16:9: E128 continuation line under-indented for visual indent
#./PiCam.py:25:13: E128 continuation line under-indented for visual indent
#./PiCam.py:29:1: W293 blank line contains whitespace
#./PiCam.py:31:22: E225 missing whitespace around operator
#./PiCam.py:32:42: E231 missing whitespace after ','
#./PiCam.py:32:80: E501 line too long (113 > 79 characters)
#./PiCam.py:35:80: E501 line too long (101 > 79 characters)
#./PiCam.py:44:1: W293 blank line contains whitespace
#./PiCam.py:46:80: E501 line too long (93 > 79 characters)
#./PiCam.py:48:1: W293 blank line contains whitespace
#./PiCam.py:53:1: W293 blank line contains whitespace
#./PiCam.py:55:1: W293 blank line contains whitespace
#./PiCam.py:58:50: E231 missing whitespace after ','
#./PiCam.py:58:80: E501 line too long (109 > 79 characters)
#./PiCam.py:59:80: E501 line too long (116 > 79 characters)
#./PiCam.py:64:49: E231 missing whitespace after ','
#./PiCam.py:64:59: W291 trailing whitespace
#./PiCam.py:66:62: W291 trailing whitespace
#./PiCam.py:72:49: E231 missing whitespace after ','
#./PiCam.py:72:59: W291 trailing whitespace
#./PiCam.py:74:62: W291 trailing whitespace
#./PiCam.py:77:15: E111 indentation is not a multiple of 4
#./PiCam.py:79:1: E305 expected 2 blank lines after class or function definition, found 1

