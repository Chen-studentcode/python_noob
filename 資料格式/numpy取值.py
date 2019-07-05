# -*- coding: utf-8 -*-
import numpy as np
a=np.arange(1,13).reshape(3,4)

#取出每一列
for i in range(a.shape[0]):    
    print(a[i])

print('-'*25)

#取出所有元素
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(a[i][j])
    
    
    
    