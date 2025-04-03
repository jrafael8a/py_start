@echo off
mode 70,15

git add .
git commit -m "subiendo todos los cambios desde IT"
git push
gh repo sync

echo.
echo.
TIMEOUT /T 5 /nobreak