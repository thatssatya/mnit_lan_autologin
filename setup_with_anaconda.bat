echo off
cls
"%windir%\System32\cmd.exe" /k ""%ANACONDA_ROOT%\Scripts\activate.bat" "%ANACONDA_ROOT%" && cd /d %~dp0 && python "scripts\setup.py" && python "scripts\create_shortcut.py" && exit"