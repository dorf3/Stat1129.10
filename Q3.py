#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:13:01 2022

@author: ml
"""
## Question 3 ##
weather = {"Sunny": "play", "Rainy": "watch tv", "Cloudy": "walk"}
x = weather.values()
weather.update({"Snowy": "ski"})
for w in weather:
    print("When", w, "let us", weather[w])