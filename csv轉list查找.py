# -*- coding: utf-8 -*-


import csv

# =============================================================================
# 利用INDEX查找
# =============================================================================
with open('flights.csv')as csvF:
    csvdata=csv.reader(csvF)
    listcsvdata=list(csvdata)  
    
    for i in range(len(listcsvdata)):
        try:
            if listcsvdata[:][i].index('09:00')>=0:
                print(listcsvdata[:][i])
        except:
            pass

# =============================================================================
# 利用IN查找 (較正規)
# =============================================================================
with open('flights.csv')as csvF:
    csvdata=csv.reader(csvF)
    listcsvdata=list(csvdata)    
    for i in range(len(listcsvdata)):
        if '09:00' in listcsvdata[:][i]:
            print(listcsvdata[:][i])

