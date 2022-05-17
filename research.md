info about imu-errors:
    i couldnt find the right article about my problem anymore. so we'll have to work with my memorie here 
    tello drones seem to have problems when they are flying over surfaces with strong reflections (like water or my floor tiles at home).
    (the forum article with the water problem: https://tellopilots.com/threads/tello-positioning-system-not-working-correctly.1940/)
    in the end this problem throws the imu error, because the drone seems to have problems to analyse the camera footage.
    fix: just dont fly over surfaces with strong reflection or if necessary place a towel or blanket beneath.

little research for further progression: 
    -post from user pgminin (https://tellopilots.com/threads/how-can-i-detect-an-objects-distance-from-the-tello-drones-camera.4694/#:~:text=Well-known%20member,-Joined%20Jan%207&text=You%20can%20estimate%20the%20distance,and%20the%20trigonometric%20tangent%20function.)

    -a project about tracking and following a person rith a drone. (with a tello drone)
    (https://jckantor.github.io/CBE30338/B.02-Visual-Tracking-of-an-Object-with-a-Drone.html)
            -in the project the authors wirte about the importance of implementing a working remote controle. I'll guess this is one of my first objectives, writting a class which allows me to controll the drone like the tello app does. more important i could use this class to learn how to bypass the process blocking of the djitello methods and this should also help me to understand the drone and python better(hopefully)

    -a collection of keywords and explanations for programming drones/robots form STEM-Robotics. might be a good place to dig deeper into some buzzwords or tools for our project 
    (https://stemrobotics.cs.pdx.edu/taxonomy/term/166)

