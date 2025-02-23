"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd


def pregunta_03():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")  # Leer el archivo con pandas
    return df["c1"].value_counts().sort_index()  # Contar ocurrencias y ordenar alfabéticamente


# Ejecutar la función y mostrar el resultado
print(pregunta_03())