import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('reporte_hurto_policia.csv')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Deparamentos con mayor cantidad de hurtos
print("\nDepartamentos con mayor cantidad de hurtos:")
print(df['DEPARTAMENTO'].value_counts().head(5))

# Municipios con mayor cantidad de hurtos
print("\nMunicipios con mayor cantidad de hurtos:")
print(df['MUNICIPIO'].value_counts().head(5))

# Bogota posee 3,36 mas poblacion que Cali 
# A pesar de esto en proporción Cali tiene 1,5 veces mas hurtos que Bogota por cada 100.000 habitantes
#en bogota roabn a 1 de cada 116 personas
#en cali roban a 1 de cada 85 personas
# aunque en villavicencio parece ser que roban a uno de cada 33 personas