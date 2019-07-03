# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:24:12 2019

@author: User
"""

a=['a','b','c','d']
b=[1,2,3,4]

#轉清單
zip_ab =zip(a,b)
list_ab=list(zip_ab)
print(list_ab)

#轉字典 製作字典時方便使用
zip_ab =zip(a,b)
dict_ab=dict(zip_ab)
print(dict_ab)

#反打包
zip_ab =zip(a,b)
unzip_ab=zip(*zip_ab)
print(list(unzip_ab))
