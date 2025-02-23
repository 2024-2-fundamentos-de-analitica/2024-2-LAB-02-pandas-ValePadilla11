"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_09():
    # Load the TSV file from the correct directory
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # Extract the year manually to avoid errors
    df["year"] = df["c3"].str[:4]  # Extracts first 4 characters (year)

    return df  # ✅ Return the full DataFrame

# Execute and print for testing
print(pregunta_09().tail())