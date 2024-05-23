import os
import pandas as pd
from db_connection import ConnectionBD, insert_dataframe_to_sql
from data_extraction import process_products
from utils import calculate_discount
from dotenv import load_dotenv

# Se carga las variables de mi archivo .env
load_dotenv()

# Ruta para las imágenes poner aqui la ruta de ASSETS ya que cuando exporte tenga la ruta y con clic le habra la imagen esto 
# lo hice por que si se va enviar a un usuario y quiere ver la imagen se puede alojar en una carpeta compartida y con clic lo puede ver

assets_path = r"C:\Users\ING ANGEL\Desktop\PRUEBA ANALISTA DATOS\ASSETS"
os.makedirs(assets_path, exist_ok=True)

# URLS a procesar
urls = [
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/fh.html",
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/vm-fe-fl.html",
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/fm-fmx.html",
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/reparacion-de-caja-vt2514b.html",
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/motor-volvo.html",
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/skandipower.html",
    "https://volvorepuestos.com.pe/repuestos-camiones-volvo/volvo-connect.html"
]

# Procesar cada URL y guardar los datos
all_product_data = []
for url in urls:
    product_data = process_products(url, assets_path)
    all_product_data.extend(product_data)

# Se Crea un DataFrame se elimina los duplicados ya que se va repetir la info al enviarla al sql o bajarla al excel y se calcula el descuento
df_volvo = pd.DataFrame(all_product_data)
df_volvo = df_volvo.drop_duplicates(subset='CODIGO_DE_PRODUCTO')
df_volvo['DESCUENTO'] = df_volvo.apply(calculate_discount, axis=1)

# Verifico la coneccion a mi bd  y inserto los datos 
connection_insert = ConnectionBD()

if connection_insert:
   table_name = "RepuestosVolvo"  
   insert_dataframe_to_sql(df_volvo, table_name, connection_insert)

# Guardo el df en csv y json
df_volvo.to_csv('Repuestos.csv', index=False)
df_volvo.to_json('Repuestos.json', orient='records')


