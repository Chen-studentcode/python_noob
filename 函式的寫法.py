# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:03:24 2019

@author: User
"""

a=lambda x:x*3  #lambda寫法

def b (x):      #標準寫法
    x=x*3
    return x

print(a(3))
print('*'*20)
print(b(3))
print('-'*20)

c=lambda x,y:x+y #lambda寫法

def d (x,y):     #標準寫法
    d=x+y
    return d

print(c(2,3))
print('*'*20)
print(d(2,3))
