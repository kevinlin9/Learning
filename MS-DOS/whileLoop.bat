@echo off
rem BAT code is white space sensitive
rem This is a while loop
color 02
set start=0
set plus=1
set end=10
:loop
echo %start%
set /a start= %start% + %plus%
if %start%==%end% goto close
goto loop
:close
echo done
pause