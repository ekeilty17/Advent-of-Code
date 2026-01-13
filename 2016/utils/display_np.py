import numpy as np
from numpy.typing import NDArray

def display_np_str(arr: NDArray[str], supress: bool=False) -> str:
    out = []
    for row in arr:
        out.append("".join(row))
    out_str = "\n".join(out)
    if not supress:
        print(out_str)
    return out_str

def display_np_int(arr: NDArray[int], supress: bool=False) -> str:
    return display_np_str(arr.copy().astype(str), supress)

def display_np_bool(arr: NDArray[bool], true_str: str="#", false_str: str=".", supress: bool=False) -> str:
    arr = np.where(arr.copy(), true_str, false_str)
    return display_np_str(arr, supress)