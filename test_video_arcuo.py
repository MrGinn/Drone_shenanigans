""" Read video frames from drone, detect markers and show detections using cv2.imshow(). """
import time
import tkinter
import cv2
from djitellopy import Tello

#initialize window
#window = tkinter.Tk()
#window.title = "Tellosamas Camfeed"
#window.mainloop()

#initialize drone
tellosama = Tello()
tellosama.connect()

#viewing cam
tellosama.streamon()
frame_reader = tellosama.get_frame_read()

for i in range(360):
    
    print(type(frame_reader.frame))
    cv2.imshow("Window", frame_reader.frame)
    cv2.waitKey(int(1/30 * 1000))


tellosama.streamoff()
