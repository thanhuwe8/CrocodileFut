@echo off

set SCRIPTDIR=%~dp0
set LIBDIR = %E:/ProgramData/Anaconda3/
set PYTHONPATH=%LIBDIR%

(
call cd /d ".CrocodileFut/"
echo "Set script dir to %SCRIPTDIR% and python path to %LIBDIR%"
call C:\ProgramData\anaconda3\Scripts\activate.bat
echo "Activate environment: "
echo "Running: python - m main.py"
call conda activate CrocodileFut
call python ./main.py
@REM python main.py %*
)



cmd /k
