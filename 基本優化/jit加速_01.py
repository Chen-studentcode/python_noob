

import numpy as np
from numba import jit
import time

start_time = time.time()
@jit(nopython=True)
def tightbind3D(n, t, a):    
    result = []
    
    Pi = 3.1415926311
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result.append(-2*t*(np.cos((-Pi/a)+i*(2*Pi)/(n*a)) + np.cos((-Pi/a)+j*(2*Pi)/(n*a)) + np.cos((-Pi/a)+k*(2*Pi)/(n*a))))
    return result

tightbind3D(100,1,1)
print(time.time() - start_time)

del start_time

# =============================================================================
# 下方未使用JIT
# =============================================================================

start_time = time.time()
def tightbind3D(n, t, a):    
    result = []
    
    Pi = 3.1415926311
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result.append(-2*t*(np.cos((-Pi/a)+i*(2*Pi)/(n*a)) + np.cos((-Pi/a)+j*(2*Pi)/(n*a)) + np.cos((-Pi/a)+k*(2*Pi)/(n*a))))
    return result

tightbind3D(100,1,1)
print(time.time() - start_time)