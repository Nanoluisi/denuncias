import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('reporte_hurto_policia.csv')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Resumen estadístico del DataFrame
print("\nResumen estadístico del DataFrame:")
print(df.describe())

# Conteo de valores únicos en cada columna
print("\nConteo de valores únicos en cada columna:")
print(df.nunique())

# Conteo de valores en la columna "TIPO DE HURTO"
print("\nConteo de valores en la columna 'TIPO DE HURTO':")
print(df['TIPO DE HURTO'].value_counts())

# Promedio de la columna "CANTIDAD"
print("\nPromedio de la columna 'CANTIDAD':")
print(df['CANTIDAD'].mean())

# Frecuencia de valores en la columna "GENERO"
print("\nFrecuencia de valores en la columna 'GENERO':")
print(df['GENERO'].value_counts())

# Frecuencia de valores en la columna "GRUPO ETARIO"
print("\nFrecuencia de valores en la columna 'GRUPO ETARIO':")
print(df['GRUPO ETARIO'].value_counts())
