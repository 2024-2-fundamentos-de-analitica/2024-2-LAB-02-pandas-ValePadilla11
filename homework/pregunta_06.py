"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd


def pregunta_06():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")  # Leer el archivo
    valores_unicos = sorted(df["c4"].str.upper().unique())  # Convertir a mayúsculas y ordenar
    return valores_unicos

# Ejecutar la función y mostrar el resultado
print(pregunta_06())