# Fifa 23: CrocodileFut


## Intro
This project is a trading bot that buys and sells players on the FUT (FIFA Ultimate Team) Transfer Market web application. 

Built in Python, this bot uses [Selenium](https://www.selenium.dev/documentation/en/) to interact with FUT Webapp via [ChromeDriver](https://www.chromium.org/) and uses [Tkinter](https://wiki.python.org/moin/TkInter) as user interface


## Overview & Features
CrocodileFut facilitate different kinds of methodology to trade in the market. Some methodologies including but not limited to:
- Buy Low get High 
- Follow the trend (SBC supply demand etc.)
- Statistical arbitrage between different data providers (FUTBIN, FUTWIZ, FUTHEAD, WEFUT etc.)
- Market making special card
- Sniping high-end card

Algorithms can be executed within UI with bid war or sniping war, with random generator waiting time and customized setup (wait time, search per loop, break, etc.):

<img src="./WebResources/UI.png" >

## Running the bot
If you have python, just install required packages, modify the main.cmd file. Below is example from mine

```console
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
```

## Guide for developers

I used Visual studio code with conda packages management as below:

```console
conda create --name CrocodileFut
conda activate CrocodileFut
conda list -n CrocodileFut
conda list


conda install pandas
conda install selenium
pip install tk
pip install ttkbootstrap
pip install undetected-chromedriver
pip install webdriver-manager
```
 The workspace path is setup as follow:

<img src=".WebResources/VScode workspace.png">

## Roadmap for EAFC24: Any improvement, ideas are welcomed!