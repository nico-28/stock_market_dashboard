import yfinance as yf
import pandas as pd
import sqlite3
import os
from datetime import datetime

# Activos seleccionados (mercado tradicional)
tickers = ['AAPL', 'GLD', 'JPM']

# Descargar datos de los últimos 2 días en intervalos de 1h
data = yf.download(
    tickers=tickers,
    period='2d',
    interval='1h',
    group_by='ticker',
    auto_adjust=True,
    threads=True
)

# Lista para almacenar los DataFrames de cada activo
resultados = []

for ticker in tickers:
    df = data[ticker].copy()
    df = df.reset_index()
    df['ticker'] = ticker
    df = df.sort_values('Datetime')

    # Cálculo de KPIs
    df['close'] = df['Close']
    df['volume'] = df['Volume']
    df['var_pct'] = df['close'].pct_change() * 100
    df['volatility_daily'] = df['close'].rolling(window=6).std()
    df['return_daily'] = df['close'].pct_change(periods=6) * 100

    # Selección de columnas
    df_final = df[['ticker', 'Datetime', 'close', 'volume', 'var_pct', 'volatility_daily', 'return_daily']]
    df_final = df_final.dropna(subset=['close', 'volume'])  # Permitimos NaNs en KPIs si es necesario

    resultados.append(df_final)

# Concatenar todo en un solo DataFrame
df_all = pd.concat(resultados)

# Guardar en base SQLite (mismo nombre que usa Power BI)
db_path = 'precios.db'
conn = sqlite3.connect(db_path)
df_all.to_sql('precios_hora', conn, if_exists='replace', index=False)
conn.close()

# Verificar ubicación del archivo
print("\n✅ Base actualizada correctamente con KPIs diarios.")
print("📁 Ruta del archivo .db actualizado:")
print(os.path.abspath(db_path))

try:
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Python ejecutado correctamente\n")
except Exception as e:
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error en Python: {e}\n")
        
