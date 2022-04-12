# SYSC 3010

# Project Idea: DOR
# Group L1-G6
## Marwan Zeyada, 101141759
## Aymaan Newaz, 101165043
## Mohamed Selim, 101138926
## TA: Victoria Ajila

#### About:
The DOR is an automated door controller that can be controlled with a click of a button. 
The system operates on four different devices:
1. The GUI: The GUI sends user instruction to an online database. 
2. Scheduler: The core program of DOR. The Scheduler pulls the instructions from the database and relays them to the mechanical components of the system at the proper times. It also controls the PiCamera that determines the status of the door by comparing it to the reference image taken while setting up. 
3. Door Opening Pi: Uses a 5V stepper motor that opens it through a string
4. Door Closing Pi: Uses a 12V DC motor that will have its speed efficiency controlled by a L928N motor driver controller module. 
It comes in the form of an Android app that with multiple functionalities.  
The product consists of 2 motors, 3 Raspberry Pi's, 1 PiCam, 2 motor controllers that are moved using string that is connected to the motors. 

#### Set-Up Instructions:


