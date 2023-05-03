# Plansul Dia das mães

![Python - Version](https://img.shields.io/badge/python-3.10-green)

Automação do photoshop através de arquivo .txt para a geração de imagens em jgp de acordo com o nome e foto da mãe e filho

# Objetivo

Facilitar a criação de arquivos para homenagem das colaboradoras que são mãe na Plansul, utilizando um arquivo criado préviamente no photoshop `.psd`, com as camadas `foto1`, `foto2`, `foto3` e `foto4` para troca das fotos e as camadas `texto1`, `texto2`, `texto3` e `texto4`

# Instalação

```shell 
$ pip install -r requirements.txt
```

# Tecnologias utilizadas

No projeto utilizamos _python_ como linguagem de programação, o programa Adobe Photoshop do windows e as bibliotecas _pyautogui_ para coleta de informações de informação do path do usuario, _photoshop.api_ para interação do algoritmo com o _Adobe Photoshop_ e a biblioteca _Pillow_ para redimensão de imagens

# Como utilizar

Certifique-se que tem o _Python_ e _Adobe Photoshop_ estão intalados <br> 
Insira a imagens a serem substituidas na pasta `resources/images` <br>
Insira o nome e o path separados por virgula no arquivo `nome_e_path.txt` <br>
Copie o path da pasta onde está salvo os arquivos<br>
Abra o cmd ou algum bash em seu computador e navegue até a pasta do arquivo<br>
Execute o programa _main.py_<br>
```shell
$ python3 main.py
```
Espere abrir o prompt e faça o input do path dos arquivos <br>
