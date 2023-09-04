@echo off

set SCRIPTDIR=%~dp0
set LIBDIR = %E:/ProgramData/Anaconda3/
set PYTHONPATH=%LIBDIR%

(
call cd /d "E:\Workspace\Github Codebase\CrocodileFut\src"
echo "Set script dir to %SCRIPTDIR% and python path to %LIBDIR%"
call E:\ProgramData\Anaconda3\Scripts\activate.bat
echo "Activate environment: "
echo "Running: python - m main.py"
python main.py %*
)

cmd /k
