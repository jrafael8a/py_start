@echo off
echo ========================================
echo Git Pull y Merge Forzado con Estrategias
echo ========================================

:: Intentar hacer un pull normal
echo 1. Intentando hacer un git pull normal:
git pull
if %ERRORLEVEL% NEQ 0 (
    echo El git pull normal fallo, intentando forzar el merge con la estrategia 'theirs'...
    
    :: Si el pull falla, forzar el merge con la estrategia "theirs"
    git pull --strategy-option theirs
    if %ERRORLEVEL% NEQ 0 (
        echo El merge con la estrategia 'theirs' fallo, intentando forzar el merge con la estrategia 'recursive'...
        
        :: Si eso también falla, forzar el merge con la estrategia "recursive"
        git pull --strategy=recursive --strategy-option=theirs
        if %ERRORLEVEL% NEQ 0 (
            echo ERROR: El pull y el merge siguen fallando. Verifica los conflictos manualmente.
        ) else (
            echo Merge exitoso con la estrategia 'recursive'.
        )
    ) else (
        echo Merge exitoso con la estrategia 'theirs'.
    )
) else (
    echo Pull exitoso y merge realizado sin conflictos.
)

echo ========================================
echo Script completado.
pause
