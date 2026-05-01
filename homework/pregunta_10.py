"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

from pathlib import Path
import pandas as pd


data_dir = Path(__file__).resolve().parent.parent / "files" / "input"


def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    tbl0 = pd.read_csv(data_dir / "tbl0.tsv", sep="\t")
    result = tbl0.groupby("c1")["c2"].apply(lambda s: ":".join(s.astype(str).sort_values().tolist())).to_frame()
    result.index.name = "_c1"
    return result
