
__doc__ = '''
le programme permet d'exercuter des exprexion reguliére un
sur des fichier precis salut
'''
from repertoire import cmds,effter
effter()


def resltat(title:str='expression reguliére',_:str = '') -> str:
    '''formatage du texte'''
    return f'{title:-^62}\n|{'': ^60}|\n|{_: ^60}|\n|{'': ^60}|\n{'':-^62}'

reg = input('entrer un expression reguliére : ')
# file = input('fichier : ')
file = '*.*'
cmd = f'findstr /n {reg} {file}'

effter()
print(resltat(_=cmd))
cmd = cmds(cmd)
if not cmd:
    print(resltat(title='resultat',_='aucun resultat'))
    exit()
cmd = cmd.split(':')
file =''
for _ in cmd:
    if reg in _ and cmd[cmd.index(_)-1].isdigit():
        pos = _.index(reg)
        ag = 3 if (len(_) - pos+len(reg)) > 3 else 0
        _ = _[pos : len(reg) + ag] + '...'
        file += f'|{_:->20}{'': >40}|\n'
    else : 
        file += f'|{_:->20}{'': >40}|\n'

print(resltat(title='resultat',_=file[1:-2]))