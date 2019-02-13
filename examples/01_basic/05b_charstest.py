# CharsTest is a feature of the driver allowing you to see every of the
# characters available in a font definition .
#
#
from ili9341.tests import BaseTests

l = BaseTests(baud = 21000000 ) # step down the SPI bus speed to 21 MHz may be opportune when using 150+ mm wires

# Draw characters in black on white background for CONFORTABLE READING.

l.fillMonocolor(WHITE)
l.charsTest(color = BLACK, font = 'Arial_14')
