#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:15:32 2020

@author: pcheewe1
"""
import pandas as pd
import numpy as np

def position_FBLR(lower, upper, choice):
    if choice == "F" or choice == "L":
        position = lower + (upper-lower)//2
        return (lower, position)
    elif choice == "B" or choice == "R":
        position = upper - (upper-lower)//2
        return (position, upper)
    else:
        return False

def position_func(x, lower, upper):
    for choice in x:
        (lower, upper) = position_FBLR(lower, upper, choice)
    if lower == upper:
        return lower
    else:
        return (lower, upper)

df = pd.read_csv("data_day5.txt", names = ["data"])
df["input_list_FB"] = df["data"].apply(lambda x: x[0:7])
df["input_list_LR"] = df["data"].apply(lambda x: x[7::])

df["output_FB"] = df["input_list_FB"].apply(lambda x: position_func(x, 0, 127))
df["output_LR"] = df["input_list_LR"].apply(lambda x: position_func(x, 0, 7))

#part1 answer
df["part1"] = df["output_FB"]*8 + df["output_LR"]
part1 = df["part1"].max()

#part2
possible_seats = set([i for i in range(df["part1"].min(), df["part1"].max()+1)])
occupied_seats = set(df["part1"].values.tolist())
print(possible_seats - occupied_seats)