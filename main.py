import photoshop.api as ps
from photoshop import Session
import pyautogui
import sys, os
from os import walk, path
from time import sleep
sys.path.insert(0, './src')

# path input
prompt = pyautogui.prompt(text='digite o caminhho do arquivo psd', title='photoshop', default='C:/Users/thegu/Documentos/Mother-day-py/')
caminho = os.path.join(prompt, 'resources/cartaz_mae.psd');

# open photoshop on path inputed
app = ps.Application()
app.load(caminho)

# read bd file
with open('nomes_e_path.txt', 'r') as arquivo:
    index = 0
    index2 = 1
    for linha in arquivo:
        nome = linha.split(',')[0]
        origem_img = os.path.join(prompt, 'resources/images')
        img = linha.split(',')[1]

        # change text layer
        with Session() as ps:
            doc = ps.active_document
            layername = 'texto' + str(index + 1)
            text_layer = doc.artLayers.getByName(layername)
            text_layer.textItem.contents = str(nome)
        
        # find which image to replace
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

        # open image as replace
        pyautogui.click(68,17, duration=0.5)
        pyautogui.click(60,405, duration=0.5)
        pyautogui.click(125,49)
        pyautogui.write(origem_img)
        pyautogui.press('enter')
        pyautogui.click(307,420, duration=0.5)
        pyautogui.write(img)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.press('enter')
        # save document
        pyautogui.hotkey('ctrl', 's')
        sleep(3)

        # close window
        pyautogui.hotkey('ctrl', 'w')

        # incremento
        index += 1

        # test for save or not and save
        if index % 4 == 0:
            index = 0
            options = ps.JPEGSaveOptions(quality=5)
            nomeimg = "imagem" + str(index2)
            jpg_file = os.path.join(prompt, "resources/files", nomeimg + ".jpg")
            doc.saveAs(jpg_file, options, asCopy=True)
            index2 += 1