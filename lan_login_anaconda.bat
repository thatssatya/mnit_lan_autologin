echo off
cls
"%windir%\System32\cmd.exe" /k ""%ANACONDA_ROOT%\Scripts\activate.bat" "%ANACONDA_ROOT%" && python "scripts\login.py" && exit"