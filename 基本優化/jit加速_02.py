# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:34:59 2019

@author: Carson
"""
import numba as nb
import time

# 普通的 for
def add1(t):
    start = time.time()
    s=0
    for i in range(t):
        s+=i
    onlytime=time.time()-start
    return  onlytime

# pthon 內建函式
def add2(t):
    start = time.time()
    s=sum(range(1, t))
    onlytime = time.time() - start
    return  onlytime

# 使用 jit 加速後的 內建函式
@nb.jit()
def add_with_jit(t):
    start = time.time()
    s = sum(range(1, t))
    onlytime = time.time() - start
    return onlytime

# 使用 jit 加速後的 for
@nb.jit()
def add_with_jitf(t):
    start = time.time()
    s = 0
    for i in range(t):
        s += i
    onlytime = time.time() - start
    return onlytime

print("普通的for迴圈: {}".format(add1(100000000)))                  
print("普通的for迴圈+jit: {}".format(add_with_jitf(100000000)))     
print("python內建函式: {}".format(add2(100000000)))                 
print("python內建函式+jit: {}".format(add_with_jit(100000000)))     



