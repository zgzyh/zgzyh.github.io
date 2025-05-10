@echo off
chcp 65001 > nul

REM 先运行Python脚本生成禁点并启动引擎
python random_ban.py

REM 原启动命令（可选，如果需同时启动Lizzie界面）
REM start jre\java11\bin\javaw.exe -jar lizzie.jar

pause