# Importing Image and ImageGrab module from PIL package
from PIL import Image, ImageGrab
import pyautogui
import extcolors
import time

vacant = (124, 124, 124)

# using the grab method
dino = ImageGrab.grab(bbox=(1080, 350, 1200, 400))
# dino.show()
color = extcolors.extract_from_image(dino)


while True:
    # time.sleep(0.2)
    dino = ImageGrab.grab(bbox=(1080, 350, 1200, 400))
    # dino.show()
    color = extcolors.extract_from_image(dino)
    print(color[0][1][0])
    if color[0][1][0] != vacant:
        pyautogui.press('space')
        print('jump', color[0][1][0])

# my browser is open side by side (right side) of my pycharm. \
# if you use the full screen of the mode, you will need to adjust the
# ImageGrab(bbox) frame. visit https://chromedino.com/ for the dino game.