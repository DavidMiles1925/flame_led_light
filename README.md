# Dumpster Fire - Flame With Flickering LEDs

## Project Description

![Flicker](./media/Flicker.gif)

This is the code portion of a project I am doing for a 3D printing contest entry. The code is meant to activate several RGB LEDs to create a flickering, flame-like effect.

## Supplies

### Supply List

| Item                   | Qty | Link                                                                                                      |
| ---------------------- | --- | --------------------------------------------------------------------------------------------------------- |
| 3D Print File          | 1   | [Creality](https://www.crealitycloud.com/user-profile/5069172030)                                         |
| Raspberry Pi           | 1   | [Microcenter](https://www.microcenter.com/product/683270/raspberry-pi-raspberry-pi-zero-w-2-with-headers) |
| Solderless BreadBoard  | 1   | [Amazon](https://www.amazon.com/gp/product/B07LFD4LT6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)    |
| Dupont M-F Cables      | 14  | [Amazon](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)    |
| 220 Ohm Resistor       | 12  | [Amazon](https://www.amazon.com/gp/product/B07ZX2CB6B/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)    |
| 470 Ohm Resistor       | 8   | [Amazon](https://www.amazon.com/gp/product/B07ZX2CB6B/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)    |
| 1K Ohm Resistor        | 4   | [Amazon](https://www.amazon.com/gp/product/B07ZX2CB6B/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)    |
| RGB LED (Common Anode) | 4   | [Amazon](https://www.amazon.com/gp/product/B09BHSDDZ5/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)    |

### Choosing an LED - Common Cathode vs Common Anode

You will find that there are two main types of RGB LEDs out there. The type you buy will affect the way the device needs to be wired and coded.

**I used a common ANODE LED for this project, but you can use either.** I will make some notes later on regarding what changes to make if you are using a common cathode LED.

![Common Anode](./media/RGB_LED_common_anode.jpg)

## Circuit and Power

I will use the 5V rail on the RPi, and divide it into one parallel circuit for each LED to connect to the anode. I will run the RPi pins to the ground pins of each LED individually.

**IMPORTANT: USE THE CORRECT RESISTOR VALUES TO AVOID DAMAGE TO YOUR PI!** The Rapsberry Pi comes with current limitations. Each GPIO pin should only carry a maximum of **16mA**, and the total GPIO should not carry a current greater than **50mA**.

### RGB LED Resistor Values:

**Red: 1220 Ohms** ((5V-2V)\1220 = 2.5mA)
**Green: 690 Ohms** ((5V-3.2V)\690 = 2.6mA)
**Blue: 690 Ohms**((5V-3.2V)\690 = 2.6mA)

**Total Current Through GPIO with 4 RGB LED units: ~30mA**

**_WARNING: THIS SIMPLIFIED IMAGE IS JUST TO ILLUSTRATE THE VALUE OF RESISTORS NEEDED, NOT THE FINAL CONFIGURATION._**

![Resistors](./media/breadboard_with_labels.jpg)

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

![Pinout](./media/pinout_pi_zero.png)

**_Note, because I used a common ANODE LED I am running power from the 5V rail to the anode of the LED. If you were to use a common cathode, you would need to run the cathode to a ground pin on the Pi._**

![Wired](./media/pi_wired_up_new.jpg)

## Setting up the Raspberry Pi

### Setup Instructions

If you have never used a Raspberry Pi before, here are some resources I have created over the years that may be helpful for you.

**[My GitHub - Setting up a Raspberry Pi]**(https://github.com/DavidMiles1925/pi_zero_setup?tab=readme-ov-file#setting-up-raspberry-pi-zero)

**[My YouTube - Setting up a Raspberry Pi]**(https://youtu.be/PFzUDpfFmyg)

### Installing Git

Run this code from your terminal.

```bash
sudo apt install git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## Downloading and Running the Code

**1. Clone the Repository**

Run this command from your home folder to clone the repository:

```bash
git clone https://github.com/DavidMiles1925/flame_led_light.git
```

**2. Set up `config.py`**

You can edit `config.py` with the command:

```bash
sudo nano config.py
```

When you are finished press Ctrl+S followed by Ctrl+X to save and exit.

Adjust `FLICKER TIME` to set the time (in seconds) between light changes. The default is 0.05 seconds.

If you use different pins than this tutorial specifies, you'll need to update the pin numbers in `config.py`.

**3. Modify code if needed for common cathode**

Remove (or comment out) lines 21-27 in `main.py`. Un-comment lines 13-18 of the code.

**4. Test the code**

Navigate into the program's directory. From there, run the command:

```bash
sudo python main.py
```

Debug for your set up if necessary.

**5. Set the program to run on startup**

You'll need to edit your `rc.local` file on your Raspbery Pi. Add this line to the file before the `exit` code. Replace YOUR_PI_NAME with the name of your Pi.

```bash
sudo python /home/YOUR_PI_NAME/flame_led_light &
```

**DO NOT FORGET THE "&" AT THE END!**

## 3D Print

### Link to 3D Model Files:

If you want to print the dumpster that goes along with this project, it can be found here:

[Creality](https://www.crealitycloud.com/user-profile/5069172030)

### Gallery

![Dumpster Fire GIF](./media/Dumpster_Fire.gif)

![Front](./media/front.jpg)

![Brain and Print](./media/dumpster_and_brain.jpg)

![Back](./media/back.jpg)

![Inside](./media/wire_dumpster_fire.jpg)

![Cord Hole](./media/cord_hole.jpg)
