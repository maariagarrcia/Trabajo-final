#Importamos la librería pandas 
import pandas as pd 
df_datos = pd.read_csv(r"output.csv") # Leemos el archivo csv
#print(df_datos)
#Traducimos los nombres de las columnas de nuestros datasets para facilitar el trabajo
df_datos.rename(columns = {"Entity": "Entidad",
"Code": "Identificador",
"Year": "Año",
"Deaths": "Muertes",
"Sidness": "Lateralidad"})