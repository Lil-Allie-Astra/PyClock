@ECHO OFF

IF "%1"=="test" goto :TEST
IF DEFINED "%1" goto :START
goto :BLANK

:START
start "My PyClock" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py" "%1" "%2"
timeout /t 1 >NUL
nircmd win setsize ititle "My PyClock" 3840 -492 640 183
goto :EOF
exit

:BLANK
start "My PyClock" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py"
timeout /t 1 >NUL
nircmd win setsize ititle "My PyClock" 3840 -492 640 183
goto :EOF
exit

:TEST
start "PyClock White" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py" "1" "5"
start "PyClock Color" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py" "3" "6"
start "PyClock Crazycolor" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py" "4" "10"
start "PyClock Solidcolor Cycle" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py" "2" "15"
start "PyClock 1-color" cmd /c "mode con: cols=78 lines=9 && python "%CD%\PyClock.py" "5" "5"
timeout /t 1 >NUL
rem nircmd win setsize ititle "Pyclock White" 3840 -492 640 183
rem nircmd win setsize ititle "Pyclock Color" 3840 -309 640 183
rem nircmd win setsize ititle "Pyclock Crazycolor" 3840 -126 640 183
rem nircmd win setsize ititle "Pyclock Solidcolor Cycle" 3840 57 640 183
rem nircmd win setsize ititle "Pyclock 1-color" 3840 240 640 183
exit
