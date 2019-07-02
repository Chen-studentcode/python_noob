# -*- coding: utf-8 -*-
        
import math
from time import time 
t = time() 

def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

# Test
nums = range(100000)
for n in range(100):
    r = compute_roots(nums)
    
print("total run time:")
print(time()-t)
del math
# =============================================================================
#下方僅取用部分模組
# =============================================================================

from math import sqrt

t = time() 
def compute_roots(nums):

    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

nums = range(100000)
for n in range(100):
    r = compute_roots(nums)
    
print("total run time:")
print(time()-t)
