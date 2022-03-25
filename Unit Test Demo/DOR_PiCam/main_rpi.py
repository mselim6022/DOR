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
