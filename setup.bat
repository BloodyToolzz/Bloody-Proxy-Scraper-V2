@echo off
color 0C

pip install -r requirements.txt
echo Done!
del requirements.txt
del setup.bat
pause