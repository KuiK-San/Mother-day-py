from PIL import Image

img = Image.open('c:/Users/thegu/Documentos/Mother-day-py/resources/images/mae1.png')
img_resized = img.resize((240, 240))
img_resized.save('c:/Users/thegu/Documentos/Mother-day-py/resources/images/oi.png')