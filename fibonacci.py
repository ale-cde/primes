# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:44:55 2019

@author: alejandro
"""
#fibonacci
a=int(input())
l=[0,1]
for i in range (2,a+1):
  b=l[i-1]+l[i-2]
  l.append(b)
k=l[1:]
print(k)