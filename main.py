import pyautogui as pag
from PIL import ImageGrab 
import time
import random

"""
###############################
## VARIABLE DEFINITIONS.
## Ajust variables as needed.
###################################
"""
# Colors of the mine floor
GROUND_COLORS  = [(103, 80, 76, 255), (94, 70, 67, 255)]

# Mining region coordinates (x, y)  
MINPOINT = (840, 700)
MAXPOINT = (960, 870)

# Time (in seconds) to spend mining in place.
MINING_TIME = 30

# Average walking time (in seconds).
AVERAGE_WALKING_TIME = 2.5

def mine():
    # Get random position within the defined mining area
    x, y = random.randint(MINPOINT[0], MAXPOINT[0]), random.randint(MINPOINT[1], MAXPOINT[1]) 
    
    # Using pillows imagegrab module to get the mining region
    image = ImageGrab.grab((x - 5, y - 5, x + 5, y + 5))
    
    # Uncomment this if you want to check which color is being grabbed
    # image.show()

    # Prevent accidental clicks on other penguins
    color = (0, 0, 0)
    for dx in range(10):
        for dy in range(10):
            color = image.getpixel((dx, dy))
            if color not in GROUND_COLORS:
                print("NOT VALID COLOR: %s" % (str(color)))
                print("Looking for new location...")
                return
            
    # Click to walk 
    print("Walking to: x: %s, y: %s" % (str(x), str(y)))
    print("Ground Color: %s" % (str(color)))
    pag.click(x, y)

    time.sleep(AVERAGE_WALKING_TIME + random.uniform(-1.0, 1.0)) 

    # Start mining (assumes you have your mining helmet on, if you don't the penguin will dance instead)
    print("Mining started...")
    pag.press("d") 

    # Time spent mining
    time.sleep(MINING_TIME + random.uniform(-5.0, 5.0))

    print("Done mining, finding new place to mine...")
    
# Don't run the script if it's being used as a module.
if __name__ == "__main__":
    while True:
        mine()