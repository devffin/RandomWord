@echo off
setlocal
cd /d "%~dp0"
py -3 -m venv .build-venv
if errorlevel 1 goto :failed
".build-venv\Scripts\python.exe" -m pip install -r requirements-build.txt
if errorlevel 1 goto :failed
".build-venv\Scripts\python.exe" -m PyInstaller --noconfirm --clean --onedir --windowed --name RandomWord main.py
if errorlevel 1 goto :failed
copy /y words.txt "dist\RandomWord\words.txt" >nul
if errorlevel 1 goto :failed
copy /y LICENSE "dist\RandomWord\LICENSE" >nul
if errorlevel 1 goto :failed
copy /y README.md "dist\RandomWord\README.md" >nul
if errorlevel 1 goto :failed
".build-venv\Scripts\python.exe" -m pip freeze > "dist\RandomWord\build-requirements.txt"
if errorlevel 1 goto :failed
echo Build complete: dist\RandomWord\RandomWord.exe
exit /b 0
:failed
echo Build failed. Review the error above.
exit /b 1
