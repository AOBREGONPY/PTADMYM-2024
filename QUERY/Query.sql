USE QA

CREATE SCHEMA pDataPrueba;
GO
DROP TABLE pDataPrueba.RepuestosVolvo 

CREATE TABLE pDataPrueba.RepuestosVolvo 
(
    CODIGO_DE_PRODUCTO	VARCHAR(512)  PRIMARY KEY,
    DESCRIPCION	VARCHAR(512),
    PRECIO_BASE	VARCHAR(512),
    PRECIO_CON_DESCUENTO	VARCHAR(512),
    IMAGEN_DEL_PRODUCTO	VARCHAR(512),
    DESCUENTO	VARCHAR(512)
);

select * from pDataPrueba.RepuestosVolvo 

CODIGO_DE_PRODUCTO
PE2 20001979
PE2 20002048
PE2 20002067
PE2 20002071

SELECT name FROM sys.databases;
GO
