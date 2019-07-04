# -*- coding: utf-8 -*-



def test_args(*args):      #值或LIST
    for i in args:
        #print(i)
        for j in i:
            print(j)
    
a=[1,2,3]
b=[4,5,6]
test_args(a)
print('*'*20)
test_args(a,b)

def test_kwargs(**kwargs):    #有鍵和值
   for k, v in kwargs.items():
      print('Optional argument %s (*kwargs): %s' % (k, v))
      

test_kwargs(a=3,b=4,d=5)



