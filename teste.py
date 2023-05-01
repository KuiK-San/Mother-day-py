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
        with Session() as ps:
            doc = ps.active_document
            layername = 'texto' + str(index + 1)
            text_layer = doc.artLayers.getByName(layername)
            text_layer.textItem.contents = str(nome)
        index += 1
        if index % 4 == 0:
            pyautogui.alert(text='cansei')
            index = 0
            options = ps.JPEGSaveOptions(quality=5)
            nomeimg = "imagem" + str(index2)
            jpg_file = os.path.join("E:/Users/thegu/Documents/ps_py/resources/files", nomeimg + ".jpg")
            doc.saveAs(jpg_file, options, asCopy=True)
            os.startfile(jpg_file)
            index2 += 1