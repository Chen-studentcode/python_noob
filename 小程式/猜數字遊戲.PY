# -*- coding: utf-8 -*-


import random 
n_01=[];t_01=0;BB=0
def startgame():
#   n_01=[]
    while len(n_01)<4:
        ra_01=str(random.randint(0,9))
        if ra_01 in n_01:
            next
        else:
            n_01.append(ra_01)
        
startgame()
print('歡迎來到猜數字遊戲，請輸入4位數字')
print('A表示數字與位置相同，B表示數字正確但位置不同')
for i in range(10):
    JJ=0;n_02=[];AA=0
    w_01=input('請輸入你的數字:')
    n_02=list(w_01)
    if n_01[0]==n_02[0]:
        AA+=1
    elif n_01[1]==n_02[1]:
        AA+=1
    elif n_01[2]==n_02[2]:
        AA+=1
    elif n_01[3]==n_02[3]:
        AA+=1
    elif AA==4 :
        print('恭喜答對!')
        break
    for j in range(4):
        JJ=JJ+(n_02[j] in n_01)
        BB=JJ-AA
    print('A:{}  B:{}'.format(AA,BB))    

print('遊戲結束!')
input('按Enter離開')


        
        