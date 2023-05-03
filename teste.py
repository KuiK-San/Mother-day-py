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

imagem = os.path.join(prompt, 'resources/images/mae2.png')



# selecionou a foto1
docRef = app.activeDocument
activeLayerName = docRef.activeLayer.name
docRef.activeLayer = docRef.layers.item('foto3')
# trocando imagem
with Session() as ps:
    replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
    desc = ps.ActionDescriptor
    idnull = ps.app.charIDToTypeID("null")
    desc.putPath(idnull, imagem)
    ps.app.executeAction(replace_contents, desc)
#renomeando layer
docRef.activeLayer.name = 'foto3'