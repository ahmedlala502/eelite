@echo off
setlocal
set "ROOT=%~dp0.."

where py >nul 2>nul
if not errorlevel 1 (
  py -3 "%ROOT%\scripts\verify_site.py" --build
  exit /b %errorlevel%
)

where python >nul 2>nul
if not errorlevel 1 (
  python "%ROOT%\scripts\verify_site.py" --build
  exit /b %errorlevel%
)

echo ERROR: Python 3 is required. Install Python and add py or python to PATH. 1>&2
exit /b 1
