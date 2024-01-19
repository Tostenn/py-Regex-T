from subprocess import run
from os import system,path
from sys import platform

def cmds(cmd):
    '''exercuter des commande shell'''
    return run(cmd,capture_output=True,text=True,shell=True).stdout.strip()

def effter():
    '''efface le terminal'''
    system("cls") if platform == "win32" else system("clear")

def __veri_chemin__(chemin:str):
    chemin = chemin if chemin else ''
    if path.exists(chemin):
        if path.isdir(chemin):return 'dossier'
        else:return 'ficher'

def __conten_fic__(chemin,l = 'r') -> str:
    verifi_ch = __veri_chemin__(chemin)
    if verifi_ch == 'ficher':
        try:
            with open(chemin,l,encoding='utf-8') as file:
                file = file.read()
        except:
            with open(chemin,l) as file:
                file = file.read()
        return file

def textToLine(file:str,text:str)-> list[int]:
    '''permet de trouver la ligne d'un texte dans un fichier ou chaîne'''
    nfois = []
    if __veri_chemin__(file) == 'ficher':
        file =  __conten_fic__(file).splitlines()
    else : file = file.splitlines()

    for i in range(len(file)):
        if text in file[i] : nfois.append(i+1)
    return nfois
