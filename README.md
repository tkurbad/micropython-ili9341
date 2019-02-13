# Micropython TFT Display Driver for ILI9341 Chipset

This is a Micropython display driver for SPI TFT displays using the
ILI9341 chipset.

The [original by @ropod7](https://github.com/ropod7/pyboard_drive/) has
been adapted to be compatible with newer Micropython versions.

This version of the driver also is specifically targeted at the ESP32
and uses one of the machine's two hardware SPI buses.

One of the advantages of ILI9341 powered screens resides in the fact
that the ILI9341 includes its own video RAM.
Thus, you don't have to rely on your microcontroller memory for drawing
and refreshing the screen, since the ILI9341 will take care of it.

The driver has been developed for the most common type of ILI9341
screens, which operate in portrait mode and have a resolution of
240 x 320 pixels.

However, resolution as well as orientation (portrait / landscape) are
configurable.

The original author did invest a lot of work in the development of this
driver. All credit for the fast drawing functions, font handling, etc.
goes to him.

# Installing the driver

To use this drivers on the pyboard:

* Copy the python file available under the /ILI9341/ (directory) to your Python Board
** eg: `lcd.py`, `colors.py` , `registers.py` , etc
* Create a `images` subfolder in the root of your pyboard to store bitmap images.
** also copy the bmp files if you plan to test example script  

## Consideration for micro SDCard

If you are planing to use some bitmap to be displayed on the TFT (yes, the driver can does it!) then we ***strongly recommand to use an micro SDCard*** as storage device.

Indeed, the pyboard embedded memory (inner flash) will immediately be surged with the first image copied on the pyboard.  

# directory structure

This section will describe the arrangement of the main directories.

* ***pyboard_drive/ILI9341/*** - the place for the pyboard files (to be copied on the Pyboard)
* ***pyboard_drive/ILI9341/images/*** - the place for the pyboard deriver images (OPTIONAL: to be copied on the pyboard)
* ***pyboard_drive/ILI9341/examples/*** - A collection of samples scripts. You do not need to copy them on the pyboard. Learn them to leverage the power of the driver.
* ***pyboard_drive/ILI9341/wirings/*** - A collection of wiring between the PyBoard and various model of TFT Screens (ILI9341 powered) 

# Resources

* [ILI9341 Datasheet](https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf) _Available at Adafruit Industries_

# About the original author @ropod7

I am just hobbyist in Python and DIY electronics. :)
