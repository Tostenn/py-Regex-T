@echo off
cls

set /p "reg=entre une expression à rechercher : "
set /p "file=ficher (defaut=*.txt) : "

if "%file%" == "" set "file=*.txt"

cls
echo -----------COMMANDE------------------
echo findstr /n %reg% %file%
echo -----------RESULTAT------------------

findstr /n %reg% %file%
echo ------------END----------------------