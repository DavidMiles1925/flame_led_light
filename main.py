import random
import time
from gpiozero import RGBLED

from config import \
RED_LED_1, \
GRN_LED_1, \
BLU_LED_1, \
RED_LED_2, \
GRN_LED_2, \
BLU_LED_2

# If you are using a common CATHODE use these values
#leds = [
#    RGBLED(red=17, green=27, blue=22),  # LED 1
#    RGBLED(red=5, green=6, blue=13),    # LED 2
#    RGBLED(red=19, green=26, blue=16),   # LED 3
#    RGBLED(red=12, green=20, blue=21),   # LED 4
#    RGBLED(red=23, green=24, blue=25),   # LED 5
#    RGBLED(red=18, green=4, blue=3)      # LED 6
#]

#colors = {
#    "white": (1, 1, 1),
#    "yellow": (1, 1, 0),
#    "orange": (1, 0.5, 0),
#    "red": (1, 0, 0)
#}

# If you are using a common ANODE use these values
leds = [
    RGBLED(red=RED_LED_1, green=GRN_LED_1, blue=BLU_LED_1, active_high=False),  # LED 1
    RGBLED(red=RED_LED_2, green=GRN_LED_2, blue=BLU_LED_2, active_high=False),    # LED 2
    #RGBLED(red=19, green=26, blue=16, active_high=False),  # LED 3
    #RGBLED(red=12, green=20, blue=21, active_high=False),  # LED 4
    #RGBLED(red=23, green=24, blue=25, active_high=False),  # LED 5
    #RGBLED(red=18, green=4, blue=3, active_high=False)     # LED 6
]

colors = {
    "white": (0, 0, 0),
    "yellow": (0, 0, 1),
    "orange": (0, 0.5, 1),
    "red": (0, 1, 1)
}


def flicker_leds():
    while True:
        # Select a random LED and color
        led = random.choice(leds)
        color = random.choice(list(colors.values()))
        
        # Apply the color to the selected LED
        led.color = color
        
        # Wait for 0.1 seconds before changing another LED
        time.sleep(0.1)



if __name__ == "__main__":
    try:
        print("Program Started")
        flicker_leds()
    
    except Exception as e:
        print("Top level exception")
        print(e)

    except KeyboardInterrupt:
        print("Program Stopped")
        for led in leds:
            led.off()