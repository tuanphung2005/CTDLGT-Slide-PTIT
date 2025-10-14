@echo off
setlocal enabledelayedexpansion

for /f "delims=" %%G in ('where git 2^>nul') do (
    set "GIT=%%G"
    goto :foundGit
)

:foundGit

set "commitMsg="
set "filesToAdd="

for /f "delims=" %%f in ('"%GIT%" ls-files -o --exclude-standard') do (
    set "path=%%f"
    if /I "!path:~-3!"==".py" (
        for %%A in ("!path!") do (
            set "base=%%~nA"
            if defined commitMsg (
                set "commitMsg=!commitMsg!,!base!"
            ) else (
                set "commitMsg=!base!"
            )
        )
        set "filesToAdd=!filesToAdd! "%%f""
    )
)

if not defined commitMsg (
    echo No new .py files to commit.
    exit /b 0
)

echo Adding: !filesToAdd!
"%GIT%" add !filesToAdd!
"%GIT%" commit -m "!commitMsg!"

endlocal