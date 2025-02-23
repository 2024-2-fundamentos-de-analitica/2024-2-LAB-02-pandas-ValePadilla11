"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_13():
    # Leer los archivos
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    # Hacer el merge usando c0 como clave
    merged_df = tbl0.merge(tbl2, on="c0")

    # Agrupar por c1 y sumar c5b
    result = merged_df.groupby("c1")["c5b"].sum()

    return result

# Ejecutar la función y mostrar el resultado
print(pregunta_13())