"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

from pathlib import Path
import pandas as pd


data_dir = Path(__file__).resolve().parent.parent / "files" / "input"


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    tbl0 = pd.read_csv(data_dir / "tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv(data_dir / "tbl2.tsv", sep="\t")
    merged = pd.merge(tbl0[["c0", "c1"]], tbl2[["c0", "c5b"]], on="c0")
    return merged.groupby("c1")["c5b"].sum().sort_index()
