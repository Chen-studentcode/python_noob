# -*- coding: utf-8 -*-


import csv

# =============================================================================
# 標準轉換
# =============================================================================
with open('flights.csv')as csvF:    
    listCsvdata=list(csv.reader(csvF))  
    dictCsvdata={}    
    for i in range(len(listCsvdata)):
        dictCsvdata[listCsvdata[i][0]]=[listCsvdata[i][1],listCsvdata[i][2]]
     
     
    
# =============================================================================
# Comprehension
# =============================================================================
with open('flights.csv')as csvF:    
    listCsvdata=list(csv.reader(csvF))  
    dictCsvdata2={}    
    dictCsvdata2={j[0]:[j[1],j[2]]  for j in listCsvdata}
    
    
