import pyautogui as py
from time import sleep
import os
from pynput.mouse import Listener
import threading

class AutoBot():
    def __init__(self):
        self.caminho = 'C:\\Users\\Documentos\\Desktop\\wasp\\imgs'
        os.chdir(self.caminho)

        self.img_mana = 'mana.png'
        self.img_mana_baixa = 'mana_baixa.png'
        self.img_health = 'health.png'
        self.img_yellow_health = 'yellow_health.png'
        self.img_red_health = 'red_health.png'
        self.img_mana_muito_baixa = 'mana_muito_baixa.png'
        self.wasp = 'wasp.png'
        self.img_hole = 'hole.png'
        self.img_rope = 'rope.png'
        self.img_down = 'down.png'
        self.img_up = 'up.png'




        self.listener = None
        self.x = None
        self.y = None

        sleep(5)


    def hole(self):
        hole = py.locateCenterOnScreen(self.img_hole, confidence=0.7)
        if hole is not None:
            py.moveTo(hole)
            py.click()
            sleep(5)
            down = py.locateCenterOnScreen(self.img_down,confidence=0.7)
            py.moveTo(down)
            py.click()

    def up(self):
        up = py.locateCenterOnScreen(self.img_up,confidence=0.7)
        if up is not None:
            py.moveTo(up)
            py.click()
            sleep(5)
            py.press('1')
            rope = py.locateCenterOnScreen(self.img_rope, confidence=0.7)
            py.moveTo(rope)
            py.press('f7')
            py.click()



bot = AutoBot()
bot.hole()