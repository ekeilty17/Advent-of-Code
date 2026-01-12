import numpy as np
from numpy.typing import NDArray

def display_np_str(arr: NDArray[str]) -> str:
    out = []
    for row in arr:
        out.append("".join(row))
    out_str = "\n".join(out)
    print(out_str)
    return out_str

def display_np_int(arr: NDArray[int]) -> str:
    return display_np_str(arr.copy().astype(str))

def display_np_bool(arr: NDArray[bool], true_str: str="X", false_str: str=".") -> str:
    arr = np.where(arr.copy(), true_str, false_str)
    return display_np_str(arr)