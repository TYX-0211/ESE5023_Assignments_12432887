#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:13:32 2024

@author: apple
"""

#Flowchart-from large to small
def Print_values():
    x=0
    y=0
    z=0
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    
    if (a>=b):
        x=a
        y=b
    else:
        x=b
        y=a
        
    if (c<y):
        z=c
    elif(c>=y and c<x):
        z=y
        y=c
    else:
        z=y
        y=x
        x=c
    print(x+y-10z)
        
        
        
        
    
        
    