# -*- coding: utf-8 -*-

import pandas as pd


# =============================================================================
# 常見的格式與基本取值
# =============================================================================
a=[['a',1,1],['b',2,2],['c',3,3],['d',4,4]]
b=['a','b','c','d','e','f']

c=pd.DataFrame(a)   #轉成DataFrame格式 
c.columns=['A欄','B欄','C欄']  #設定columns標題
c.set_index('A欄',inplace=True)  #設定index

d=pd.Series(b)      #轉Series格式 (二微陣列)

print(c.loc['c'])           #找出index是c的
print('')
print(c.loc[['c','a']])    #找出index是c和a的
print('')
print(c.iloc[2])         #找出index位置是2的
print('')
print(c.iloc[2:4])          #找出index位置是2到3的

    


