# -*- coding: utf-8 -*-

import numpy as np

a=list(np.arange(1,15))
b=['A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4','D1','D2']
list_1=[]

def Calculation():
    [list_1.append([A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2]) \
     for A2 in a for B2 in a for C2 in a for D2 in a \
     if len(set((A2,B2,C2,D2)))==4 and A2/B2/C2==D2 \
     for C1 in a for C3 in a for C4 in a \
     if len(set((A2,B2,C2,D2,C1,C3,C4)))==7 and C1*C2*C3==C4 \
     for A3 in a for B3 in a if len(set((A2,A3,B2,B3,C2,D2,C1,C3,C4)))==9 and A3+B3+C3==15 \
     for A1 in a for B1 in a for D1 in a \
     if len(set((A1,A2,A3,B1,B2,B3,C1,C2,C3,C4,D1,D2)))==12 and A1+B1-C1==D1\
     for A4 in a if len(set((A1,A2,A3,A4,B1,B2,B3,C1,C2,C3,C4,D1,D2)))==13 and A1+A2-A3==A4\
     for B4 in a if len(set((A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2)))==14 and B1+B2-B3==B4]
    
    dict_1=dict(zip(b,list_1[0]))
    for k,v in dict_1.items():
        print(f'{k}:{v}')

Calculation()
