from CYD import CYDBoard
from ili9341 import Display, color565

cyd = CYDBoard()

def save_callback(self):
    print("SAVE Button pressed!")

def exit_callback(self):
    print("EXIT Button pressed!")
    
#cyd.display.fill_hrect(10,10,80,40,color565(255,255,255))
cyd.button(10,10,80,40,'SAVE',color565(200,50,0),color565(255,255,255),save_callback)
cyd.button(10,50,80,40,'EXIT',color565(200,250,50),color565(255,255,255),exit_callback)

while True:
    cyd.ts.get_touch()
