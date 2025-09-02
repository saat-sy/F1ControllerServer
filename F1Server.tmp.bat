@echo off
REM Navigate to the server directory
cd /d "pwd"

REM Activate the Python virtual environment 
call venv\Scripts\activate.bat

REM Run the Python server
python server.py

REM Keep the window open after execution
pause