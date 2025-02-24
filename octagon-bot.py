import pyautogui
import time
import pygame
from pynput.keyboard import Key, Controller, Listener
import keyboard


pygame.init()
screen = pygame.display.set_mode((100, 100))

pynkey = Controller()

print ("Running")
while True:
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    #print(r, g, b, x, y)
    d_x, d_y = 720, 600
    print(pyautogui.pixel(d_x, d_y))


    def on_press(key):
        if hasattr(key, 'char') and key.char == 'g':
            print("g key pressed")
        if key == Key.enter:
            start_octagon_macro();

    listener = Listener(on_press=on_press)
    listener.start()

    time.sleep(0.001)

def start_octagon_macro():
    while True:
        continue