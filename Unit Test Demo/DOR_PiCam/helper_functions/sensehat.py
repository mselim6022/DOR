from sense_hat import SenseHat
from time import sleep
#This function creates and returns an instance of a SenseHat
def get_sensehat():
  sense = SenseHat()
  return sense


def alarm(sense, flash_time):
  for i in range (flash_time):
    if (i%2 == 1):
      sense.clear()
    else:
      sense.clear(255,0,0)
    sleep(1)
  sense.clear()

