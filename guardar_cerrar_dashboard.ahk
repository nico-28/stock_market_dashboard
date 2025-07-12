; Esperar que Power BI esté activo
WinWaitActive, stocks_dashboard - Power BI Desktop
Sleep, 3000

; Guardar
Send, ^s
Sleep, 2000

; Cerrar Power BI
Send, !{F4}

; Agregar log
FormatTime, timestamp,, yyyy-MM-dd HH:mm:ss
FileAppend, [%timestamp%] Power BI guardado y cerrado correctamente`n, C:\Users\HP\OneDrive\Escritorio\stock_market_dashboard\logs.txt
