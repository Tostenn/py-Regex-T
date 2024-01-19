try:
    # ce module est uniquement disponible pour les client prenium
    from repertoire import cmds,effter,__conten_fic__,textToLine 
except:
    print('vous ne disposer pas du module repertoire\n\
          Vous pouvez coder tout les fonctions manquantes\
          ou me contacter pour une meilleur approche')
    exit()
from re import findall
from time import time
from PIL import Image
from pytesseract import image_to_string,pytesseract

effter()

# couleur -------------
CODE_COLOR = '\x1b[38;5;'
color = {
    'or':CODE_COLOR+'190m',
    'gr':CODE_COLOR+'244m',
    'bl':CODE_COLOR+'15m',
    'fr':CODE_COLOR+'87m',
    'rg':CODE_COLOR+'3m',
    'vt':CODE_COLOR+'5m',
}

def resltat(title:str='expression reguliére',_:str = '',cl:str=color['or']) -> str:
    '''formatage du texte'''
    return f'{color['gr']}{f"{color['bl']}{title}{color['gr']}":-^88}\n|{'': ^65}|\n|{f'{cl}{_}{color['gr']}': ^87}|\n|{'': ^65}|\n{f'{color["fr"]}T_xOx_T{color['gr']}':-^88}{color['bl']}'


# Spécifiez le chemin d'accès à l'exécutable Tesseract OCR 
# (changez cela selon votre installation)
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
EXT_IMG = ['png','jpg','jpeg']
def imgToText(image_path):
    '''extrait le texte d'une image'''
    # Ouvrir l'image
    image = Image.open(image_path)

    # Utiliser Tesseract OCR pour extraire le texte de l'image
    text = image_to_string(image)

    return text


reg = input('entrer un expression reguliére : ')

# recherche fichier  --------
files = input('fichier : ')
dir = 'dir /b '
sfile = input('inclure les sous répertoire [o/n] : ').lower()
if sfile == 'o':
    dir += '/s '
dir += files

# effacer le terminal ----------------
effter()

# temps t1 ---------------
t1 = time()

# regex et fichier ciblées ----------------
print(resltat(_=f'{reg} ==> {files}')) 

# recuperation des fichiers -----------------
files = cmds(f'dir {dir}').splitlines() 
regFile = r'[\S ]+\.(?=(png|jpg|jpeg))'
container = ''
for file in files:
    if findall(regFile,file):content = imgToText(file)
    else : 
        try:content = __conten_fic__(file)
        except:content = ''
    if not content: continue # pass if le fichier est binaire
    regs = set(findall(reg,content))
    for _ in regs:
        line = [str(i) for i in textToLine(content,_)]
        container += f":{file}:line=>{','.join(line)}:{_}:"
# exit()
# aucun resultat -------------
if not container:
    print(resltat(title='resultat',_='aucun resultat'))
    exit()

# formatage des resultats -------------
container = container.split(':')
content = ''
for _ in container:
    content += f'|{color["gr"]}{f'{color["vt"]}{_}{color["gr"]}':->50}{'': >35}|\n'
t1 = time()-t1
content += f'|{f't {t1:.2f}ms':->30}{'': >35}|\n'

print(resltat(title='resultat',_=content[1:-2],cl=''))
