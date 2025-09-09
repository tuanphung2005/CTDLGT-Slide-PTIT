@echo off
setlocal enabledelayedexpansion
set "msg="
for /f "delims=" %%f in ('git status --porcelain') do (
    set "line=%%f"
    set "file=!line:~3!"
    echo !file! | findstr /E ".py" >nul
    if not errorlevel 1 (
        set "name=!file:.py=!"
        set "msg=!msg! !name!"
    )
)
if not defined msg (
    echo where .py man where.
    exit /b
)
git add .
git commit -m "!msg:~1!"