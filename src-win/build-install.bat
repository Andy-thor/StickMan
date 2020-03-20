@echo off
setlocal enabledelayedexpansion enableextensions
set EXIT_STATUS=0
set EXE=mintty.exe
REM Don't edit these sentences!
REM ===========================
set DIR_MSYS=%SystemDrive%\msys64
if exist %DIR_MSYS% (
    goto setup
) else (
    EXIT_STATUS=25
    goto failed
)

:setup
REM Download and installation of its dependencies
set filecontent=
set ignore_conf=--noconfirm
set CURRENT_SCRIPT_DIR=%~dp0
set _file=%CURRENT_SCRIPT_DIR%packages-dep.txt

if not exist %_file% (
    EXIT_STATUS=3
    goto failed
)
for /f  %%a in (%_file%) do (
    set "currentline=%%a "
    set "filecontent=!filecontent!!currentline!"
)

set f_keep_tmp=.keep-tmp
set home=%DIR_MSYS%\home\%USERNAME%
REM set loop_proc=while [[ $(ps -ef | grep "pacman -S") != "" ]] ; do var=""; done
REM set cmd_update="rm -f %f_keep_tmp%; touch %f_keep_tmp%; pacman -Syu --ignore pacman %ignore_conf% 2>&1; rm %f_keep_tmp%; exit"
REM set cmd_update="touch %f_keep_tmp%; pacman -Syu %ignore_conf% 2>&1; sleep 3; rm -f %f_keep_tmp%; exit"
set cmd_update=pacman -Syu %ignore_conf% 2>&1; sleep 3
REM set cmd_install_pkgs="rm -f %f_keep_tmp%; touch %f_keep_tmp%; pacman -S %ignore_conf% %filecontent%; rm %f_keep_tmp%; exit"
set cmd_install_pkgs="touch %f_keep_tmp%; pacman -S --needed %ignore_conf% %filecontent% 2>&1; sleep 10; rm %f_keep_tmp%; exit"
REM set msysshell=msys2_shell.cmd
set bashshell=usr\bin\bash.exe
set pathshell=%DIR_MSYS%\%bashshell%
if not exist %pathshell% (
    EXIT_STATUS=4
    goto failed
)
REM This section is to prevent console stay bugged
if "%1%"=="first-update" goto firstupdate
goto :FIRST

REM The first time it will crash
:firstupdate
start /b cmd.exe /c %pathshell% -l -c "rm -f %f_keep_tmp%;%cmd_update%; exit"
set next=1000
timeout /t 30
goto WAITLOOP

:FIRST
start /b cmd /c %pathshell% -l -c "touch %f_keep_tmp%;%cmd_update%;rm -f %f_keep_tmp%; exit"
set next=2
timeout /t 30
goto WAITLOOP

REM We retry because the terminal has a bug that ends suddenly.
:SECOND
start /b cmd /c %pathshell% -l -c "touch %f_keep_tmp%;%cmd_update%;rm -f %f_keep_tmp%; exit"
set next=3
timeout /t 3
goto WAITLOOP

:THIRD
start /b cmd /c %pathshell% -l -c %cmd_install_pkgs%
set next=1000
timeout /t 3
goto WAITLOOP

:WAITLOOP
if exist %home%\%f_keep_tmp% goto RUNNING
goto NOTRUNNING

:RUNNING
goto WAITLOOP
:NOTRUNNING
if %next% equ 2 goto SECOND
if %next% equ 3 goto THIRD

:DONE
echo All done!
exit /b 0

:failed
echo *** FAILED ***
exit /b %EXIT_STATUS%



REM pacman -Syu --ignore pacman
REM pacman -Su --ignore pacman --force
