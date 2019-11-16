'''
Created on Nov 2, 2019

@author: ITAUser
'''
from test.test_enum import Fruit
from _ast import If
i = 2
while i <  6:
    print(i)
    if i == 3:
        break
    i += 1
    
fruits = ["apple","blueberry","raspberry"]
for fruit in fruits:
    print(fruits)
    if fruits == "blueberry":
        break

n = 5
for i in range(n):
    for j in range(i):
        print("*",end = "")
    print("")