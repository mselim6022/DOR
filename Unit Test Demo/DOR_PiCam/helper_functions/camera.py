from picamera import PiCamera
from time import sleep

def get_camera():
  camera = PiCamera()
  return camera

def camera_preview(camera, preview_time):
  camera.start_preview()
  sleep(preview_time)
  camera.stop_preview()

def rotate_camera(camera, degrees):
  camera.rotation = degrees
  
def capture_image(camera, image_out_location, countdown_time = 0, preview = False):
  if(preview):
    camera.start_preview()
  sleep(countdown_time)
  camera.capture(image_out_location)
  camera.stop_preview()
  
def capture_video(camera, video_out_location, video_length, countdown_time = 0, preview = False):
  if(preview):
    camera.start_preview()
  sleep(countdown_time)
  camera.start_recording(video_out_location)
  sleep(video_length)
  camera.stop_recording()
  camera.stop_preview()
