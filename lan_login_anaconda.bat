echo off
cls
"%windir%\System32\cmd.exe" /k ""%ANACONDA_ROOT%\Scripts\activate.bat" "%ANACONDA_ROOT%" && cd /d %~dp0 && python "scripts\login.py" && exit"