# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:44:55 2019

@author: alejandro
"""
#%%
#primos
a=10
l=[]
for i in range (1,a+1):
  for j in range (2,i):
    if i%j == 0:
      break
  else:
    l.append(i)
print(l)
# %%
