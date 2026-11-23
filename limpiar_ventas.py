"""Limpia un CSV de ventas desordenado con pandas.

Uso:
    python limpiar_ventas.py ventas_practica.csv
Genera ventas_limpias.csv en la misma carpeta.
"""
import sys
import pandas as pd

archivo = sys.argv[1] if len(sys.argv) > 1 else "ventas_practica.csv"
df = pd.read_csv(archivo)

# 1. Nombres: quitar espacios y unificar mayúsculas
df["cliente"] = df["cliente"].str.strip().str.title()

# 2. Precio: quitar "$", cambiar coma decimal por punto y pasar a número
df["precio"] = (df["precio"].str.replace("$", "", regex=False)
                            .str.replace(",", ".", regex=False)
                            .astype(float))

# 3. Fechas: hay dos formatos (AAAA-MM-DD y DD/MM/AAAA); se leen por separado
iso = pd.to_datetime(df["fecha"], format="%Y-%m-%d", errors="coerce")
latam = pd.to_datetime(df["fecha"], format="%d/%m/%Y", errors="coerce")
df["fecha"] = iso.fillna(latam)

# 4. Eliminar filas duplicadas
df = df.drop_duplicates()

# 5. Mostrar cuántos datos faltan por columna y guardar el resultado
print("Datos faltantes por columna:")
print(df.isna().sum())
df.to_csv("ventas_limpias.csv", index=False)
print(f"Listo: {len(df)} filas guardadas en ventas_limpias.csv")
