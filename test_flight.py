""" Bring drone up an fly some meters. Display all senor readings of the drone, except video stream. """
from djitellopy import Tello

#initialize drone
tellosama = Tello()
tellosama.connect()


#giving commands
tellosama.takeoff()
tellosama.move_up(25)
tellosama.move_forward(50)
tellosama.rotate_clockwise(180)
tellosama.move_down(25)


#read and display all senorreadings 
state = tellosama.get_current_state()
for element in state:
    print(element + ":")
    print(tellosama.get_state_field(element))

#landing and shutting down the drone
tellosama.land()
tellosama.end()