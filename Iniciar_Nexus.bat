@echo off
title NEXUS: 宿命の瞳
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-ChildItem -Recurse '%~dp0' | Unblock-File" 2>nul
if exist "%~dp0Nexus.exe" (
    start "" "%~dp0Nexus.exe"
) else (
    start "" "%~dp0lib\py3-windows-x86_64\pythonw.exe" "%~dp0game"
)
