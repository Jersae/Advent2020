#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:09:25 2020

@author: pcheewe1
"""

import pandas as pd

with open('data_day6.txt') as f:
    data_list = []
    tmp = []
    for line in f:
        if line == '\n':
            data_list.append(tmp)
            tmp = []
        else:
            tmp.append(line.strip('\n'))
    if tmp ==[]:
        pass
    else:
        data_list.append(tmp)

data_list = ["|".join(data) for data in data_list]

def group_set_part1(x, delimeter = '|'):
    return set.union(*[set(i) for i in x.split(delimeter)])

def group_set_part2(x, delimeter = '|'):
    return set.intersection(*[set(i) for i in x.split(delimeter)])

df = pd.DataFrame(data_list, columns = ["data"])
df["group_set1"] =  df["data"].apply(group_set_part1)
df["group_set_count1"] = df["group_set1"].apply(len)
#part1
part1 = df["group_set_count1"].values.sum()

#part2
df["group_set2"] =  df["data"].apply(group_set_part2)
df["group_set_count2"] = df["group_set2"].apply(len)
part2 = df["group_set_count2"].values.sum()