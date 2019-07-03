# -*- coding: utf-8 -*-


# =============================================================================
# filter(function, iterable)  filter(判斷函數, 可疊代對象)
# 不會改變原始對象，回傳處理結果為filter物件須轉換
# =============================================================================

list_a=[1,2,3,4,5,6,7,8,9,10]

def odd(n):
   return n % 2== 1


#以下三種結果一致
new_list=list(filter(odd,[1,2,3,4,5,6,7,8,9,10] ))         #自訂函式,清單
new_list2=list(filter(lambda x: x % 2 == 1, list_a))    #匿名函式,清單物件
new_list3=list(filter(lambda x: x % 2 == 1, range(11))) #匿名函式,range疊代器

