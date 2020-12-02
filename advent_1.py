# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:17:51 2020

@author: Chee Wee
"""

import pandas as pd


x = pd.read_csv("expense_day1.txt", names = ["expense"])["expense"].tolist()

length_x = len(x)
while length_x > 1:
    for i in range(1, length_x):
        for j in range(2, length_x):
            if x[0] + x[i] + x[j] == 2020:
                print(x[0], x[i], x[j])
    x.pop(0)
    length_x = len(x)
