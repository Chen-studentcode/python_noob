# -*- coding: utf-8 -*-


class score():    
    def __init__(self,name=None,a=0,b=0,c=0,d=0):
        self.name = name
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.tDcore =0
        self.avgDcore=''
        
    def inputScore(self):
        self.name=input('請輸入姓名:')
        self.a=eval(input('請輸入a成績'))
        self.b=eval(input('請輸入b成績'))
        self.c=eval(input('請輸入c成績'))
        self.d=eval(input('請輸入d成績'))
        self.tDcore='總成績為:'+str(self.a+self.b+self.c+self.d)
        
    
    def outputScore(self):
        print('a成績為:',self.a)
        print('b成績為:',self.b)
        print('c成績為:',self.c)
        print('d成績為:',self.d)
        
    def avgScore(self):
        self.avgDcore=self.name+'同學的平均成績:'+str((self.a+self.b+self.c+self.d)/4)
        

student_01=score()
student_01.inputScore()
print(student_01.name)
print('*'*20)
student_01.outputScore()
student_01.avgScore()

print(student_01.avgDcore)




        
        
        
        
    