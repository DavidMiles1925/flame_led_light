# Flame With Flickering LEDs

## Project Description

This is the code portion of a project I am doing for a 3D printing contest entry. The code is meant to activate several RGB LEDs to create a flickering, flame-like effect.

## Documentation

### Circuit Power

I will use the 5V rail on the RPi, and divide it into one parallel circuit for each LED to connect to the anode. I will run the RPi pins to the ground pins of each LED individually.

**RGB LED Resistor Values:**

Red: 147
Green: 100
Blue: 100
