@echo off
REM Download MSYS2
set EXIT_STATUS=0
set output=msys2-x86_64-20190524.exe
set url=http://repo.msys2.org/distrib/x86_64/%output%
set path_file=%TEMP%\%output%
curl -C - %url% --output %path_file%

if not exist %path_file% (
    EXIT_STATUS=1
    goto failed
)

echo All done!
exit /b 0

:failed
echo *** FAILED ***
exit /b %EXIT_STATUS%
