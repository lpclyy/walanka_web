@echo off
echo Starting Walanka AI Website...
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask backend server...
start cmd /k "python server.py"

echo.
echo Starting frontend server...
start cmd /k "python -m http.server 8000"

echo.
echo Servers started successfully!
echo Frontend: http://localhost:8000
echo Backend API: http://localhost:5000
echo.
pause