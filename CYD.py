from machine import Pin, SPI, ADC, idle
from ili9341 import Display, color565
from xpt2046 import Touch

class CYD():
    """ Class for cheap yellow display LCD and TS """
    
    def __init__(self):
        self.lcd = None
        # Function to set up SPI for TFT display
        display_spi = SPI(1, baudrate=60000000, sck=Pin(14), mosi=Pin(13))
        # Set up display
        display = Display(display_spi, dc=Pin(2), cs=Pin(15), rst=Pin(15),
                          width=320, height=240, rotation=lcd_rotation)
        display.clear(black_color)
        display.fill_hrect(0,0,80,40,color565(255, 255, 255))
 
