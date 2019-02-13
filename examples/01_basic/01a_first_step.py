# In this sample we will:
# * initialize the driver
# * Set the background 
# * Load a Bitmap image at RGR565 format.
#   The image must be present in the "images" sub-directory of your pyBoard 
#
from ili9341.lcd import *

l = LCD(baud = 21000000) # step down the SPI bus speed to 21 MHz may be opportune when using 150+ mm wires                                                    
l.fillMonocolor( GREEN)                                                    
l.renderBmp('test.bmp')
