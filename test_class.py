from CYD import CYDBoard
# import this to convert color codes the LCD will understand
from ili9341 import color565

# Create the cyd object
cyd = CYDBoard()

# This function will get called by the cyd object after we create a button for it
def save_callback(self):
    print("SAVE Button pressed!")

# This function will get called by the cyd object after we create a button for it
def exit_callback(self):
    print("EXIT Button pressed!")
    
# Create a button object that will be displayed on the LCD and monitored for button presses inside it
# the button is created @ 10,10 and is 80 pixels wide by 40 pixels high. The first color is the button color
# the second is the text color and the last parameter is the callback method
cyd.button(10,10,80,40,'SAVE',color565(200,50,0),color565(255,255,255),save_callback)
cyd.button(10,50,80,40,'EXIT',color565(200,250,50),color565(255,255,255),exit_callback)

# call the touschscreen get_touch method to check for keypresses.
# When a button is pressed, its callback method will be called
while True:
    cyd.ts.get_touch()
