from collections.abc import Callable
import numpy as np
from math import exp

def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:
    ret = np.empty(t.shape)
    for i in range(len(t)):
        ret[i] = f(t[i])
    return ret

def func(t: float) -> float:
    if t < 0:
        return 0
    elif t <= 3:
        return exp(-t)
    elif t <= 4:
        return exp(-3*t)
    else:
        return 0

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
