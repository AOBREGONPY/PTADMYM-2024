import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def ConnectionBD():
    try:
        connection_string = f"mssql+pyodbc://{os.getenv('SQL_SERVER_USER')}:{os.getenv('SQL_SERVER_PASSWORD')}@{os.getenv('SQL_SERVER_HOST')}/{os.getenv('SQL_SERVER_DATABASE')}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = create_engine(connection_string)
        connection_bd = engine.connect()
        print("Conexión exitosa a la base de datos SQL Server")
        return connection_bd
    except Exception as error:
        print(f"No se pudo conectar: {error}")

def insert_dataframe_to_sql(df, table_name, connection_insert):
    try:
        df.to_sql(table_name, con=connection_insert, if_exists='append', schema='pDataPrueba', index=False)
    except Exception as e:
        print(f"Error al insertar datos en la tabla '{table_name}': {e}")
