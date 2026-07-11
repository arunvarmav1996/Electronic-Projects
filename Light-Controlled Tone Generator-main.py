# Imports go at the top
from microbit import *
import music

# Code in a 'while True:' loop repeats forever
while True:
    val = display.read_light_level()

    freq = int(200+(val/255)*(2000-200))

    music.pitch(freq, duration=20)
    
    sleep(10)
        
        

                    
