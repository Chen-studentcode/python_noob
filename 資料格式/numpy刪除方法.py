# -*- coding: utf-8 -*-
import numpy as np
# =============================================================================
# 透過numpy.delete(陣列,物件位置, 軸) 若axis=None則會變成為一維
# =============================================================================
array_a = np.arange(12).reshape(4,3)

array_1=np.delete(array_a,2,axis=1) #刪除第2欄
array_2=np.delete(array_a,2,axis=0) #刪除第2列

print(array_a) #原陣列不變化
print('-'*25)
print(array_1)
print('-'*25)
print(array_2)


# =============================================================================
# 透過匹配布林刪除陣列
# =============================================================================

array_b=np.array([True,False,True,False])  #設定為ndarray型態 **重要**

array_c=array_a[array_b]  #完整寫法為array_a[array_b,:]

print(array_a) #原陣列不變化
print('-'*25)
print(array_c)


# =============================================================================
# 多維的刪除
# =============================================================================
array_A=np.arange(48).reshape((4,4,3))
array_B=np.array([[True,False,True,True],[True,True,True,True],[False,True,True,True],[False,True,False,False]])
array_C=array_A[array_B]

print(array_A)
print('-'*25)
print(array_C)