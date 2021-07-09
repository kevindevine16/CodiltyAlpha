# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:34:43 2021

@author: Kevin.Devine
"""

def solution(A):
    counter = 0
    i = 0
    B = list(dict.fromkeys(A))
    while B[-1]-A[i] != 0:
        counter +=1
        i += 1
    return counter
