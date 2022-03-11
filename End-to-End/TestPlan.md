# End-to-end Communication Demo Test Plan
### We would have a device adding entries or instructions to the database. This is to simulate the function of the user sending instructions from the GUI to the database. Our scheduler will then take the instructions from the database and print them out before relaying them via TCP to the DOR. Once the DOR receives instructions, it will confirm using print statements and respond to the Scheduler by echoing the instructions back through TCP.

## Test Plan
- Sending a message to the database
- Retrieving the message from the database
- Sending messages through TCP
- Responding to messages through TCP
