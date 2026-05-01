"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

from pathlib import Path
import pandas as pd


data_dir = Path(__file__).resolve().parent.parent / "files" / "input"


def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    tbl0 = pd.read_csv(data_dir / "tbl0.tsv", sep="\t")
    return tbl0.groupby("c1")["c2"].max().sort_index()
