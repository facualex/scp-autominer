# auto mining script

# make sure you have the following modules
import pyautogui as pag
import time
import random
from PIL import Image, ImageGrab # we only want imagegrab module

# (103, 80, 76)
# Colors of the mine floor. Adjust as needed.
GROUND_COLORS  = [(107, 79, 79, 255), (103, 76, 72, 255), (99, 72, 69, 255), (95, 69, 69, 255),
                  (103,80, 76, 255)]

# adjust this if you want to expand or shrink the mining region (x, y)  
#MINPOINT = (690, 629)
#MAXPOINT = (1130, 840)

MINPOINT = (540, 445)
MAXPOINT = (750, 530)

# Time to spend mining in place. Change as needed.
MINING_TIME = 30

# the main function
def mine():
    time.sleep(2)
    # get random position
    x, y = random.randint(MINPOINT[0], MAXPOINT[0]), random.randint(MINPOINT[1], MAXPOINT[1]) 
    
    
    # using pillows imagegrab module to get the mining region
    image = ImageGrab.grab((x - 5, y - 5, x + 5, y + 5))
    #image.show()

    # prevent accidental clicks on other penguins
    color = (0, 0, 0)
    for dx in range(10):
        for dy in range(10):
            color = image.getpixel((dx, dy))
            if color not in GROUND_COLORS:
                print("returning")
                print(color)
                return
            
    # click to walk
    print("walking to "+str(x)+", "+str(y))
    pag.click(x, y)
    time.sleep(2.5 + random.uniform(-1.0, 1.0)) # average walking time (adjust as needed)

    # start dancing which is mining in a average situation
    print("starting mining")
    pag.press("d") 

    # Time spent mining
    time.sleep(MINING_TIME + random.uniform(-5.0, 5.0))
    
# we dont want to run this if it is getting used as a module
if __name__ == "__main__":
    while True:
        mine()