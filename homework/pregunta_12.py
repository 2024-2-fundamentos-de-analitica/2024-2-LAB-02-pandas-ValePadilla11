"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_12():
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")  # Leer el archivo

    # Crear la columna c5 uniendo c5a y c5b con ":"
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)

    # Agrupar por c0 y concatenar los valores de c5 separados por ","
    grouped = df.groupby("c0")["c5"].apply(lambda x: ",".join(sorted(x)))

    return grouped.reset_index()  # Convertir la serie en DataFrame

# Ejecutar la función y mostrar el resultado
print(pregunta_12())