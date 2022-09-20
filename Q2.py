#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 23:27:22 2022

@author: ml
"""
## Question 2 ##
list = []
for i in range(0,21):
    list.append(i)
list.remove(0)
print(list)
print(len(list))
print(max(list))
print(min(list))
print(sum(list))