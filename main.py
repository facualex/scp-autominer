import pyautogui as pag
import time
import random
from PIL import ImageGrab 

# Colors of the mine floor. Adjust as needed.
GROUND_COLORS  = [(103, 80, 76, 255), (94, 70, 67, 255)]

# Adjust this if you want to expand or shrink the mining region (x, y)  
MINPOINT = (840, 700)
MAXPOINT = (960, 870)

# Time (in seconds) to spend mining in place. Change as needed.
MINING_TIME = 30

# Average walking time (adjust as needed)
AVERAGE_WALKING_TIME = 2.5

def mine():
    # get random position within the defined mining area
    x, y = random.randint(MINPOINT[0], MAXPOINT[0]), random.randint(MINPOINT[1], MAXPOINT[1]) 
    
    # using pillows imagegrab module to get the mining region
    image = ImageGrab.grab((x - 5, y - 5, x + 5, y + 5))
    
    # Uncomment this if you want to check which color is being grabbed
    #image.show()

    # Prevent accidental clicks on other penguins
    color = (0, 0, 0)
    for dx in range(10):
        for dy in range(10):
            color = image.getpixel((dx, dy))
            if color not in GROUND_COLORS:
                print("Clicked color: %s" % (str(color)))
                return
            
    # Click to walk 
    print("Walking to: x: %s, y: %s" % (str(x), str(y)))
    pag.click(x, y)

    time.sleep(AVERAGE_WALKING_TIME + random.uniform(-1.0, 1.0)) 

    # start dancing which is mining in a average situation
    print("Mining started...")
    pag.press("d") 

    # Time spent mining
    time.sleep(MINING_TIME + random.uniform(-5.0, 5.0))

    print("Done mining, finding new place to mine...")
    
# We dont want to run this if it is getting used as a module
if __name__ == "__main__":
    while True:
        mine()