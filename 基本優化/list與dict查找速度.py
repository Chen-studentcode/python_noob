# -*- coding: utf-8 -*-

from time import time 
t = time() 
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
 
print(list) 
filter = [] 
for i in range (1000000): 
     for find in ['is','hat','new','list','old','.']: 
         if find not in list: 
             filter.append(find) 
print("total run time:")
print(time()-t)

# =============================================================================
# 底下轉為字典型態執行較快
# =============================================================================
t = time()
list = dict.fromkeys(list,True) 
print(list) 
filter = [] 
for i in range (1000000): 
     for find in ['is','hat','new','list','old','.']: 
         if find not in list: 
             filter.append(find) 
print("total run time:")
print(time()-t)

