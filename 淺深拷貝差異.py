# -*- coding: utf-8 -*-
from copy import deepcopy


a=[1,2,3,[4,5]] #原始物件
b=a[:]          #淺拷貝
c=deepcopy(a)   #深拷貝

a[0]='test1'     #改變外層,只有a改變
print(f'{a}\n{b}\n{c}')
print('*'*20)

a[3][0]='test2' #改變內層,a和b都改變
print(f'{a}\n{b}\n{c}')


