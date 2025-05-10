@echo off
chcp 65001 > nul

REM 启动引擎并通过Python脚本设置禁点（异步执行）
start python random_ban.py

REM 稍等2秒，确保引擎初始化完成
timeout /t 2 > nul

REM 启动Lizzie界面（连接已运行的引擎）
start jre\java11\bin\javaw.exe -jar lizzie.jar

pause