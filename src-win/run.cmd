@echo off
set EXIT_STATUS=0
set DIR_MSYS=%SystemDrive%\msys64
set appname=StickMan
set interpreter=

if exist %DIR_MSYS% (
   set interpreter=%DIR_MSYS%\mingw64\bin\python
) ELSE (
   EXIT_STATUS = 1
   goto failed
)
set CURRENT_SCRIPT_DIR=%~dp0
set script=%CURRENT_SCRIPT_DIR%%appname%

%interpreter% "%script%"

echo All done!
exit /b 0

:failed
echo *** FAILED ***
exit /b %EXIT_STATUS%
