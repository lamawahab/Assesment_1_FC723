#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:00:53 2025

@author: lamaalabdulwahab
"""

def GCD(a,b):
    result=0
    if a==0:
        result=b
    elif b==0:
        result=a
    else:
        while a!=0 and b!=0:
            if a>b:
                big=a
                small=b
            else:
                big=b
                small=a
            int_division=big//small
            reminder=big%small
            a=small
            b=reminder
            if a==0:
                result=b
            elif b==0:
                result=a
    return result

print(GCD(270, 192))
    
                                            
                