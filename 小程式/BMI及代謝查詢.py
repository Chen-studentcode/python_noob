# -*- coding: utf-8 -*-
import time
def menu():
    try:
        print('\n歡迎使用健康小精靈~')
        print('-'*25)
        print('1.BMI計算機')
        print('2.基礎代謝率查詢')
        print('3.理想體脂肪率查詢')
        print('-'*25)
        print('0.離開')
        enter_num=int(input('請輸入欲使用的功能數字:'))
        if enter_num == 0:
            print('謝謝')
        if enter_num == 1:
            BMI()
        if enter_num == 2:
            metabolism()
        if enter_num == 3:
            Body_fat()
        if enter_num > 3:
            print('\n請輸入選項1~3')
            time.sleep(1.5)
            menu()
    except ValueError:        
        print('\n請確認輸入為數值')
        time.sleep(1.5)
        menu()
        


def BMI():
    try:
        height=float(input('請輸入身高(公尺):'))
        weight=float(input('請輸入體重(公斤):'))
        if height >= 10:
            height=height/100
        print(f'您的BMI為: {weight/height**2:.2f}')
        print('理想BMI為: 18.5 ≦BMI＜24')
        time.sleep(2.5)
        menu()
    except ValueError:
        print('請確認輸入為數值')

def metabolism():
    try:
        age=int(input('請輸入年齡:'))
        sex=input('請輸入性別(男/女):')
        weight=float(input('請輸入體重(公斤):'))
        data={'29':{'m':24,'f':23.6},'49':{'m':22.3,'f':21.7},'69':{'m':21.5,'f':20.7}}
        if sex=='男':
            sex='m'
        elif sex=='女':
            sex='f'
        else:
            print('請輸入正確性別')
        if age <=29:
            age='29'
        elif age <=49:
            age='49'
        elif age >49:
            age='69'
    except ValueError:
        print('請確認年齡/體重為數值')
        time.sleep(1.5)
        metabolism()
    
    print(f'您的基礎代謝率:{data[age][sex]*weight} kcal/day')
    time.sleep(2.5)
    menu()


def Body_fat():
    try:
        sex=input('請輸入性別(男/女):')
        data={'m':['14~20%','17-23%'],'f':['17-24%','20-27%']}
        if sex=='男':
            sex='m'
        if sex=='女':
            sex='f'

            
        print(f'小於30歲為: {data[sex][0]}')
        print(f'大於30歲為: {data[sex][1]}')
        time.sleep(3.5)
        menu()
    except KeyError:
        print('請輸入正確性別')
        time.sleep(2.5)
        Body_fat()
  
        

menu()
   






