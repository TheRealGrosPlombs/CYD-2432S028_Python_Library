import asyncio
from machine import Pin, SPI, ADC, idle
import os
from time import sleep

# Save this file as ili9341.py https://github.com/rdagger/micropython-ili9341/blob/master/ili9341.py
from ili9341 import Display, color565
# Save this file as xglcd_font.py https://github.com/rdagger/micropython-ili9341/blob/master/xglcd_font.py
from xglcd_font import XglcdFont
# Save this file as xpt2046.py https://github.com/rdagger/micropython-ili9341/blob/master/xpt2046.py
from xpt2046 import Touch

lcd_rotation = 90

# Function to set up SPI for TFT display
display_spi = SPI(1, baudrate=60000000, sck=Pin(14), mosi=Pin(13))
# Set up display
display = Display(display_spi, dc=Pin(2), cs=Pin(15), rst=Pin(15),
                  width=320, height=240, rotation=lcd_rotation)

# SPI for touchscreen
touchscreen_spi = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))

unispace_font = XglcdFont('fonts/Unispace12x24.c', 12, 24)

# Set colors (foreground) and background color
white_color = color565(255, 255, 255)  # white
black_color = color565(0, 0, 0)  # Black

# Turn on display backlight
backlight = Pin(21, Pin.OUT)
backlight.on()

# Clear display
display.clear(black_color)

buttons = {
    "SAVE": (10, 10, 80, 40),
    "EXIT": (10, 60, 80, 40)
}

for name, area in buttons.items():
    display.fill_hrect(area[0],area[1],area[2],area[3],white_color)
    # when using text8x8, we know character height is 8 and width is 8
    font_width = 8
    font_height = 8
    off_x = int((area[2] - (len(name) * font_width)) / 2)
    if off_x < 0:
        off_x = 0
    off_y = int((area[3] / 2) - (font_height / 2))
    display.draw_text8x8(area[0] + off_x, area[1] + off_y, name, black_color, white_color, 0)

# this converts the touchscreen coords to my LCD coords
def convert_ts_to_LCD(ts_x,ts_y):
    # display_lcd_rot == 270
    cx = ts_y
    cy = ts_x
    print(f"rot:{display.lcd_rot}, w:{display.width}, h:{display.height}")
    if display.lcd_rot == 0:
        cx = ts_x
        cy = display.height - ts_y
    if display.lcd_rot == 90:
        cx = display.width - ts_y
        cy = display.height - ts_x
    if display.lcd_rot == 180:
        cx = display.width - ts_x
        cy = ts_y
    return cx,cy

def touchscreen_press(tx, ty):
    print(f"ts : X = {tx:3d}, Y = {ty:3d}")
    #lcd_x, lcd_y = convert_ts_to_LCD(tx, ty)
    #print(f"lcd: X = {lcd_x:3d}, Y = {lcd_y:3d}")
    touch_point = (tx,ty)
    for name, area in buttons.items():
        if is_inside(touch_point, area):
            print(name)

# settings for my CYD. x_min, x_max, y_min, y_max are different for each touschscreen...
# you can print raw_touch() and tap each corner of screen to get your own values.
# width is the number of lcd pixels int the touschscreen X direction (not LCD orientation)
# height is the number of pixels in the touchscreen Y direction (not LCD orientation)
# These height and width should not change even if you change your LCD orientation
touchscreen = Touch(touchscreen_spi, cs=Pin(33), int_pin=Pin(36), int_handler=touchscreen_press,
                  width=240, height=320,
                    x_min=138, x_max=1858, y_min=106, y_max=1848, lcd=display)


# Check if point (x,y) is inside rect (x,y,w,h)
def is_inside(point, rect):
    """
    point: (px, py)
    rect:  (x, y, w, h)
    """
    px, py = point
    rx, ry, rw, rh = rect
    
    return rx <= px < (rx + rw) and ry <= py < (ry + rh)

async def monitor_ts():
    while True:
        await touchscreen.get_touch()
        

async def main():
    asyncio.create_task(monitor_ts())

    
if __name__ == "__main__":
    asyncio.run(main())
