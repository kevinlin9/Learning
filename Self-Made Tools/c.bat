@echo off
set i=1
set d=3
:loop
if %i%==%d% goto done
taskkill -f -im CoherentUI_Host.exe 2> nul
timeout 5 >nul
set /a i= %i% + 1
goto loop
:done
exit