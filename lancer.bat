@echo off
title ChantierManager
cd /d %~dp0

echo ============================================
echo   ChantierManager - installation / lancement
echo ============================================
echo.

REM Installe les dependances (rapide si deja installees)
python -m pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo.
    echo ERREUR : Python n'a pas ete trouve, ou l'installation a echoue.
    echo Verifie que Python est installe et accessible depuis le terminal.
    pause
    exit /b 1
)

echo.
echo Lancement de l'application...
echo Ouvre ton navigateur sur : http://localhost:5000
echo (laisse cette fenetre ouverte tant que tu utilises l'appli)
echo.

python run.py

pause
