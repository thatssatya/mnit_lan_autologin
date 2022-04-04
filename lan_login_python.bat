echo off
cls
"%windir%\System32\cmd.exe" /k "python3 "scripts/setup.py" && python3 "scripts/login.py" && exit"