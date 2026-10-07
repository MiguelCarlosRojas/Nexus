@echo off
title Desbloquear Nexus (Windows SmartScreen Bypass)
echo ===================================================
echo   NEXUS: 宿命の瞳 - Desbloqueo Seguro de Windows
echo ===================================================
echo Removiendo marca web (Mark-of-the-Web) para Microsoft Defender SmartScreen...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-ChildItem -Recurse '%~dp0' | Unblock-File; Write-Host '¡Archivos desbloqueados exitosamente! Ya puedes iniciar el juego con total normalidad.' -ForegroundColor Green"
echo.
pause
