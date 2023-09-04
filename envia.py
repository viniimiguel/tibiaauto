import pyautogui as py
from time import sleep
import os
from pynput.mouse import Listener

class AutoParcel():
    def __init__(self):
        self.caminho = 'C:\\Users\\Documentos\\Desktop\\wasp\\imgs'
        os.chdir(self.caminho)

        
        self.img_teleport = 'teleport.png'
        self.img_seled_door = 'seled_door.png'
        self.img_mail_box = 'mail_box.png'
        self.img_parcel = 'parcel.png'
        self.img_leave = 'leave.png'
        self.img_dep = 'dep.png'
        self.img_seled_door_d = 'seled_door_d.png'
        self.img_tp = 'tp.png'
        self.img_cap = 'cap.png'
        self.img_cap1 = 'cap1.png'

        sleep(5)

    def sair(self):
        lev = py.locateCenterOnScreen(self.img_leave, confidence=0.6)
        if lev is not None:
            py.moveTo(lev)
            py.click()
            sleep(20)
    def cap(self):
        c = py.locateOnScreen(self.img_cap,confidence=0.7)
        c1 = py.locateOnScreen(self.img_cap1,confidence=0.7)
        
        if c is not None:
            cp.sair()
            cp.handle_door()
            cp.teleport()
            cp.sdoor()
            cp.teleport()
        if c1 is not None:
            cp.sair()
            cp.handle_door()
            cp.teleport()
            cp.sdoor()
            cp.teleport()

    def mail(self):
        box = py.locateCenterOnScreen(self.img_mail_box, confidence=0.7)
        parc = py.locateCenterOnScreen(self.img_parcel, confidence=0.7)
        if parc is not None:
            print('Imagem do pacote encontrada!')
            py.moveTo(parc)  # Move o cursor até a posição da imagem
            py.mouseDown(button='left')   # Pressiona o botão esquerdo do mouse
            py.moveTo(box, duration=1)  # Move o cursor de volta à mesma posição para simular o arrasto
            py.mouseUp(button='left')     # Solta o botão esquerdo do mouse
        else:
            print('Imagem do pacote não encontrada')

    def locate_image_with_retries(self, image, confidence=0.6, max_attempts=4):
        for _ in range(max_attempts):
            img_location = py.locateCenterOnScreen(image, confidence=confidence)
            if img_location is not None:
                print(f'Imagem {image} encontrada!!!')
                return img_location
            else:
                print(f'Imagem {image} não encontrada. Tentando novamente...')
                sleep(2)  # Aguarda um pouco antes de tentar novamente
        return None
    
    def sdoor(self):
        msd = self.locate_image_with_retries(self.img_msd, confidence=0.5)
        msd_0 = self.locate_image_with_retries(self.img_msd1, confidence=0.5)
        
        if msd is not None:
            py.moveTo(msd)
            py.click()
            sleep(10)
            self.handle_door()
        elif msd_0 is not None:
            py.moveTo(msd_0)
            py.click()
            sleep(10) 
            self.handle_door()
        else:
            print('Nenhuma imagem encontrada')

    def handle_door(self):
        dep = self.locate_image_with_retries(self.img_seled_door, confidence=0.65)

        if dep is not None:
            py.moveTo(dep)
            py.click(dep[0], dep[1] + 15, 1, 1, button='right')

        else:
            print('Imagem da porta não encontrada!')
    def teleport(self):
        py.press('1')
        tele = self.locate_image_with_retries(self.img_tp, confidence=0.6)
        if tele is not None:
            py.moveTo(tele)
            py.click()
            sleep(5)
        else:
            print('img nao encontrada')

cp = AutoParcel()
cp.cap()
