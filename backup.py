import pyautogui as py
from time import sleep
import os
from pynput.mouse import Listener
import threading

py.FAILSAFE = False

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
        self.img_up = 'up.png'
        self.img_down = 'down.png'



        self.listener = None
        self.x = None
        self.y = None


    def detect_first_click(self):
        def on_click(x, y, button, pressed):
            if pressed:
                print(f"Clique detectado nas coordenadas (x={x}, y={y}) com o botão {button}")
                self.listener.stop()  # Para o listener após o primeiro clique
        
        with Listener(on_click=on_click) as self.listener:
            self.listener.join()

            self.x = int(input('Qual posição do X?: '))
            self.y = int(input('Qual posição do Y?: '))
            sleep(3)

    def up(self):
        up = py.locateCenterOnScreen(self.img_up, confidence=0.7)
        py.moveTo(up)
        py.click()
        sleep(6)
        py.press('f7')
        sleep(0.25)
        py.click(self.x,self.y,1,1,'left')
        rope = py.locateCenterOnScreen(self.img_rope, confidence=0.7)
        py.moveTo(rope)
        py.click()
    def hole(self):
        down = py.locateCenterOnScreen(self.img_down, confidence=0.7)
        if down is not None:
            py.moveTo(down)
            py.click()
            sleep(3)
            hole = py.locateCenterOnScreen(self.img_hole,confidence=0.7)
            py.moveTo(hole)
            py.click

    def cura(self):
        try:
            while True:
                local_mana_baixa = py.locateCenterOnScreen(self.img_mana_baixa, confidence=0.75)
                local_mana_muito_baixa = py.locateCenterOnScreen(self.img_mana_muito_baixa, confidence=0.75)
                local_mana = py.locateCenterOnScreen(self.img_mana, confidence=0.75)
                local_yellow_health = py.locateCenterOnScreen(self.img_yellow_health, confidence=0.7)
                local_red_health = py.locateCenterOnScreen(self.img_red_health, confidence=0.85) 
                local_health = py.locateCenterOnScreen(self.img_health, confidence=0.9)
                if local_mana is not None:
                    py.press('f3')
                if local_mana_baixa is not None:
                    py.press('f3')
                if local_mana_muito_baixa is not None:
                    py.press('f3')
                elif local_health is not None:
                    py.press('f1')  
                elif local_yellow_health is not None:
                    py.press('4')
                elif local_red_health is not None:
                    py.press('f2')
                else:
                    pass  # Mantém o loop executando sem ação
        except Exception as e:
            print('Erro:', e)

    def loot(self):
        py.keyDown('shift')
        for dx, dy in [(0, 0), (-42, 0), (-42, -42), (0, -42), (42, -42), (42, 0), (42, 42), (0, 42), (-42, 42)]:
            py.click(self.x + dx, self.y + dy, button='right')
        py.keyUp('shift')

    def combo(self):
        actions = [
           ('space','space'),
          
            
        ]
    
        found_battle = False  # Variável de controle
        for action in actions:
            py.press(action[0])
            py.press(action[1])
            sleep(1.85)
        
            b = py.locateCenterOnScreen('battle.png', confidence=0.6)
            if b is not None:
                print('imagem battle encontrada! parando o codigo')
                found_battle = True  # Marca a imagem como encontrada
                break  # Sai do loop
          
        if found_battle:
            pass
        else:
            pass
            
    def start(self):
        sleep(5)
        thread = threading.Thread(target=self.cura)
        thread.start()

        print('Aguarde 2 segundos e clique com o mouse no centro do seu personagem para podermos configurar o autoloot: ')
        sleep(2)

        self.detect_first_click()
        down_found = False
        is_up = True  # Variável para controlar se o bot está subindo ou descendo

        while True:
            if is_up:
                # Priorize a busca pelas imagens "primeiro.png" a "oitavo.png"
                for img_nome in ['primeiro.png', 'segundo.png', 'terceiro.png', 'quarto.png', 'quinto.png', 'sexto.png', 'setimo.png', 'oitavo.png']:
                    print('procurando imagem...')
                    local = py.locateCenterOnScreen(img_nome, confidence=0.6)
                    if local is not None:
                        py.moveTo(local)
                        py.click(local[0], local[1], button='left')
                        print('Imagem', img_nome, 'encontrada')
                        py.press('2')
                        py.press('f12')
                        sleep(4)
                        self.combo()
                        self.loot()

                # Verifique se existe um "up.png" para subir novamente
                up_found = py.locateCenterOnScreen('up.png', confidence=0.6)
                if up_found is not None:
                    is_up = True
                    print('executando a ação up')
                    self.up()  # Execute "up.png"
                else:
                    is_up = False
            else:  # Bot está descendo
                # Verifique se existe um "down.png" para descer novamente
                down_found = py.locateCenterOnScreen('down.png', confidence=0.6)
                if down_found is not None:
                    print('executando o hole')
                    self.hole()  # Execute "down.png"
                else:
                    is_up = True
                    # Se não há "down.png", execute "up.png" para subir novamente
                    up_found = py.locateCenterOnScreen('up.png', confidence=0.6)
                    if up_found is not None:
                        print('executando o up')
                        self.up()  # Execute "up.png"
                    else:
                        is_up = False





if __name__ =='__main__':
    bot = AutoBot()
    bot.start()