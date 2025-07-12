@echo off
echo [%date% %time%] Iniciando pipeline... >> logs.txt

:: Paso 1 - Ejecutar script Python para actualizar la base
call "C:\Users\HP\OneDrive\Escritorio\stock_market_dashboard\actualizar_datos.bat"
timeout /t 10

:: Paso 2 - Abrir Power BI
call "C:\Users\HP\OneDrive\Escritorio\stock_market_dashboard\abrir_dashboard.bat"
timeout /t 30

:: Paso 3 - Ejecutar AutoHotKey para guardar y cerrar Power BI
start "" "C:\Users\HP\OneDrive\Escritorio\stock_market_dashboard\guardar_cerrar_dashboard.ahk"

echo [%date% %time%] Pipeline ejecutado correctamente >> logs.txt
