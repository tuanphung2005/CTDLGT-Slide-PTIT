@echo off
for /f "delims=" %%f in ('git status --porcelain') do (
    set "line=%%f"
    setlocal enabledelayedexpansion
    set "file=!line:~3!"
    if not "!file!"=="" (
        set "msg=!msg! !file!"
    )
    endlocal
)
git add .
git commit -m "%msg%"