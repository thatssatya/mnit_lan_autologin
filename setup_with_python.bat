echo off
cls
"%windir%\System32\cmd.exe" /k "python3 "scripts/setup.py" && python "scripts\create_shortcut.py" && exit"