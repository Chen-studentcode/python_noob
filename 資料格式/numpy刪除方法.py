# -*- coding: utf-8 -*-
import numpy as np
# =============================================================================
# 透過匹配布林刪除陣列
# =============================================================================
#array_a = np.arange(12).reshape(4,3)
#array_b=np.array([True,False,True,False])  #設定為ndarray型態 **重要**
#
#array_c=array_a[array_b]  #完整寫法為array_a[array_b,:]
#
#print(array_a)
#print('-'*25)
#print(array_c)
#

# =============================================================================
# 多維的刪除
# =============================================================================
array_A=np.arange(48).reshape((4,4,3))
array_B=np.array([[True,False,True,True],[True,True,True,True],[False,True,True,True],[False,True,False,False]])
array_C=array_A[array_B]

print(array_A)
print('-'*25)
print(array_C)