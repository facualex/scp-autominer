setlocal
set "current_dir=%~dp0"
start %current_dir%\autominer-venv\Scripts\activate
"%current_dir%\autominer-venv\Scripts\python.exe" "%current_dir%\main.py"
pause