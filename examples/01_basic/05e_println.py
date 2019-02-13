# The driver allows you to draw text (string) on the screen.
# Text drawing has the following feature:
#   * Support of various font
#   * Support for text color (and background color)
#   * Cursor blinking 
#   * Draw from position (x,y)
#
from ili9341.lcd import *

l = LCD(baud = 21000000 ) # step down the SPI bus speed to 21 MHz may be opportune when using 150+ mm wires

l.fillMonocolor(RED)

# Create object that can print string on the screen
#   * initCh() create a BaseChars object which retains graphical properties about the printed string
#   * color: defines the text color
#   * font : Arial_14 by default allows you to define the font to use
#   * scale: scale the font (1, 2, 3)
#
c = l.initCh(color = BLACK, font = 'Arial_14')
p = l.initCh(color = BLACK, font = 'Arial_14', scale = 2)

# Print the strings 
#   bc: False by default, allows to show the blinking cursor when the string is printed
#   scale: scale the font (1, 2, 3)
#
c.printChar('@', 30, 30)
c.printLn('Hello BaseChar class', 30, 290)
p.printLn('Python3', 89, 155)
