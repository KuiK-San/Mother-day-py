import photoshop.api as ps
from photoshop import Session
from tempfile import mkdtemp
import pyautogui
import sys, os
from PIL import Image
from os import walk, path
from time import sleep
sys.path.insert(0, './src')


prompt = pyautogui.prompt(text='digite o caminhho do arquivo psd', title='photoshop', default='E:/Users/thegu/Documents/ps_py/resources/cartaz_mae.psd')
caminho = os.path.abspath(prompt);
app = ps.Application()
app.load(caminho)
with open('nomes_e_path.txt', 'r') as arquivo:
    index = 0
    index2 = 1
    for linha in arquivo:
        nome = linha.split(',')[0]
        origem_img = linha.split(',')[1]
        img = linha.split(',')[2]
        match index:
            case 0:
                pyautogui.click(1029,596, duration=0.5)
                sleep(0.2)
                pyautogui.doubleClick(1029,596, duration=0.5)
            case 1:
                pyautogui.doubleClick(1034,560, duration=0.5)
            case 2:
                pyautogui.doubleClick(1036,517, duration=0.5)
            case 3:
                pyautogui.doubleClick(1039,475, duration=0.5)
        pyautogui.click(68,17, duration=0.5)
        pyautogui.click(60,405, duration=0.5)
        pyautogui.click(125,49)
        pyautogui.write(origem_img)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(img)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('ctrl', 'w')
        
        with Session() as ps:
            doc = ps.active_document
            layername = 'texto' + str(index + 1)
            text_layer = doc.artLayers.getByName(layername)
            text_layer.textItem.contents = str(nome)
        index += 1
        if index % 4 == 0:
            index = 0
            options = ps.JPEGSaveOptions(quality=5)
            nomeimg = "imagem" + str(index2)
            jpg_file = os.path.join("E:/Users/thegu/Documents/ps_py/resources/files", nomeimg + ".jpg")
            doc.saveAs(jpg_file, options, asCopy=True)
            index2 += 1