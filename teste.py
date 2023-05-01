import photoshop.api as ps
from photoshop import Session
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
with Session() as ps:
    doc = ps.active_document
    layername = 'texto' + "1"
    text_layer = doc.artLayers.getByName(layername)
    text_layer.textItem.contents = "Nome da mãe"