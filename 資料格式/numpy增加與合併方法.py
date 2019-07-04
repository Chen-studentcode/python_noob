# -*- coding: utf-8 -*-
import numpy as np
# =============================================================================
# Nd.array 增加列(row , axis =0) 增加欄(column , axis =1)
# =============================================================================

array_a=np.zeros((3,4))


array_b=np.row_stack((array_a,['A','B','C','D'])) #增加列 需要兩個()

array_c=np.column_stack((array_a,['A1','B2','C3'])) #增加欄 需要兩個()

array_d=np.concatenate((array_a,array_c),axis =1) #增加欄 須為陣列物件

array_e=np.concatenate((array_a,array_b),axis =0) #增加列 須為陣列物件

print(array_a)  #原陣列不會改變
print('-'*25)
print(array_b) #增加列
print('-'*25)
print(array_c) #增加欄
print('-'*25)
print(array_d)
print('-'*25)
print(array_e)