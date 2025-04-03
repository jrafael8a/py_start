@echo off
mode 70,15

git add .
git commit -m "subiendo todos los cambios"
git push
gh repo sync

pause