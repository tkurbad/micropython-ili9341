## Constants

#   ESP32 Hardware SPI Buses
HSPI        = const(1)
VSPI        = const(2)

#   Miscelleanous
DEFAULT_BAUDRATE = const(42000000)
TFTWIDTH         = const(240)       # TFT Width
TFTHEIGHT        = const(320)       # TFT Height


#   IlI9341 registers definitions

# LCD control registers
NOP         = const(0x00)
SWRESET     = const(0x01)   # Software Reset

# LCD Read status registers
RDDID       = const(0x04)   # Read Display Identification (24-Bit)
RDDST       = const(0x09)   # Read Display Status (32-Bit)
RDDPM       = const(0x0A)   # Read Display Power Mode (8-Bit)
RDDMADCTL   = const(0x0B)   # Read Display MADCTL (8-Bit)
RDPIXFMT    = const(0x0C)   # Read Display Pixel Format (8-Bit)
RDDIM       = const(0x0D)   # Read Display Image Format (3-Bit)
RDDSM       = const(0x0E)   # Read Display Signal Mode (8-Bit)
RDDSDR      = const(0x0F)   # Read Display Self-Diagnostic Result (8-Bit)
RDID1       = const(0xDA)
RDID2       = const(0xDB)
RDID3       = const(0xDC)
RDID4       = const(0xDD)

# LCD settings registers
SLPIN       = const(0x10)   # Enter Sleep Mode
SLPOUT      = const(0x11)   # Exit Sleep Mode

PTLON       = const(0x12)   # Partial Mode ON
NORON       = const(0x13)   # Partial Mode OFF, Normal Display mode ON

INVOFF      = const(0x20)
INVON       = const(0x21)
GAMMASET    = const(0x26)
LCDOFF      = const(0x28)
LCDON       = const(0x29)

CASET       = const(0x2A)
PASET       = const(0x2B)
RAMWR       = const(0x2C)
RGBSET      = const(0x2D)
RAMRD       = const(0x2E)

PTLAR       = const(0x30)
MADCTL      = const(0x36)
PIXFMT      = const(0x3A)   # Pixel Format Set

IFMODE      = const(0xB0)   # RGB Interface Control
FRMCTR1     = const(0xB1)   # Frame Rate Control (In Normal Mode)
FRMCTR2     = const(0xB2)   # Frame Rate Control (In Idle Mode)
FRMCTR3     = const(0xB3)   # Frame Rate Control (In Partial Mode)
INVCTR      = const(0xB4)   # Frame Inversion Control
PRCTR       = const(0xB5)   # Blanking Porch ControlVFP, VBP, HFP, HBP
DFUNCTR     = const(0xB6)
ETMOD       = const(0xB7)   # Entry mode set

PWCTR1      = const(0xC0)
PWCTR2      = const(0xC1)
PWCTR3      = const(0xC2)
PWCTR4      = const(0xC3)
PWCTR5      = const(0xC4)
VMCTR1      = const(0xC5)
VMCTR2      = const(0xC7)

GMCTRP1     = const(0xE0)
GMCTRN1     = const(0xE1)
PWCTR6     =  const(0xFC)
IFCTL       = const(0xF6)
