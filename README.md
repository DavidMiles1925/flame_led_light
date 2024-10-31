# Flame With Flickering LEDs

## Project Description

This is the code portion of a project I am doing for a 3D printing contest entry. The code is meant to activate several RGB LEDs to create a flickering, flame-like effect.

## Documentation

### Circuit Power

I will use the 5V rail on the RPi, and divide it into one parallel circuit for each LED to connect to the anode. I will run the RPi pins to the ground pins of each LED individually.

**RGB LED Resistor Values:**

Adjusted Values
Red: 1220  
Green: 690  
Blue: 690

Old:

Red: 147
Green: 100
Blue: 100

### Pin Out

| LED Name  | Pin |
| --------- | --- |
| RED_LED_1 | 17  |
| GRN_LED_1 | 27  |
| BLU_LED_1 | 22  |
| RED_LED_2 | 5   |
| GRN_LED_2 | 6   |
| BLU_LED_2 | 13  |
| RED_LED_3 | 19  |
| GRN_LED_3 | 26  |
| BLU_LED_3 | 16  |
| RED_LED_4 | 12  |
| GRN_LED_4 | 20  |
| BLU_LED_4 | 21  |
| RED_LED_5 | 23  |
| GRN_LED_5 | 24  |
| BLU_LED_5 | 25  |
| RED_LED_6 | 18  |
| GRN_LED_6 | 4   |
| BLU_LED_6 | 3   |
