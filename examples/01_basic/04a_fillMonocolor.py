# fillMonocolor allows to fill the screen with a color at RGB565 format.
#
from ili9341.lcd import *

l = LCD(baud = 21000000) # step down the SPI bus speed to 21 MHz may be opportune when using 150+ mm wires

# Completely fill the screen in green
l.fillMonocolor(GREEN)
