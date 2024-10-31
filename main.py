import random
import time
from gpiozero import RGBLED

from config import \
RED_LED_1, GRN_LED_1, BLU_LED_1, \
RED_LED_2, GRN_LED_2, BLU_LED_2, \
RED_LED_3, GRN_LED_3, BLU_LED_3, \
RED_LED_4, GRN_LED_4, BLU_LED_4

# If you are using a common CATHODE use these values
#leds = [
#    RGBLED(red=RED_LED_1, green=GRN_LED_1, blue=BLU_LED_1),  # LED 1
#    RGBLED(red=RED_LED_2, green=GRN_LED_2, blue=BLU_LED_2),    # LED 2
#    RGBLED(red=RED_LED_3, green=GRN_LED_3, blue=BLU_LED_3),  # LED 3
#    RGBLED(red=RED_LED_4, green=GRN_LED_4, blue=BLU_LED_4),  # LED 4
#]


# If you are using a common ANODE use these values
leds = [
    RGBLED(red=RED_LED_1, green=GRN_LED_1, blue=BLU_LED_1, active_high=False),
    RGBLED(red=RED_LED_2, green=GRN_LED_2, blue=BLU_LED_2, active_high=False),
    RGBLED(red=RED_LED_3, green=GRN_LED_3, blue=BLU_LED_3, active_high=False),
    RGBLED(red=RED_LED_4, green=GRN_LED_4, blue=BLU_LED_4, active_high=False),
]

colors = {
    "white": (1, 1, 1),
    "purple": (1, 0, 0.3),
    "orange": (1, 0.2, 0),
    "red": (1, 0, 0),
    "red2": (1, 0, 0)
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