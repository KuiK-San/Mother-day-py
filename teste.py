import photoshop.api as ps
import pyautogui
import sys, os
from time import sleep
sys.path.insert(0, './src')
from photoshopy import Photoshopy

app = Photoshopy()
pyautogui.alert(title='Photoshop', text='Por favor Clique no photoshop antes de prosseguir', button='OK')
sleep(1)
pyautogui.hotkey('ctrl', 'o')
pyautogui.alert(title='Photoshop', text='Por favor selecione o arquivo .PSD', button='OK')
sleep(10)
para = pyautogui.confirm(title='Photoshop', text='Por favor certifiquesse que o Photoshop está aberto no arquivo cartaz_mae.psd\nA partir do momento que você pressionar OK solte o mouse e teclado até o fim da operação', buttons=['OK', 'Cancelar'])
if para == 'Cancelar':
    exit();
