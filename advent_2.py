# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:43:55 2020

@author: Chee Wee
"""

import pandas as pd




df = pd.read_csv("data_day2.txt", delimiter = ':', names = ["policy", "password"])

df["lower"] = df["policy"].apply(lambda x: int(x.split('-')[0]))
df["upper"] = df["policy"].apply(lambda x: int(x.split('-')[1].split(' ')[0]))
df["policy"] = df["policy"].apply(lambda x: x.split(' ')[1])
df["pw_number"] = df.apply(lambda x: x["password"].count(x["policy"]), axis = 1)
df["violated_1"] = df.apply(lambda x: (False if x["pw_number"]>=x["lower"] and x["pw_number"]<=x["upper"] else True), axis = 1)

x = df[df["violated_1"] == False]

df["location_1"] = df.apply(lambda x: (True if x["password"][x["lower"]] == x["policy"] else False), axis = 1)
df["location_2"] = df.apply(lambda x: (True if x["password"][x["upper"]] == x["policy"] else False), axis = 1)
y = df[(df["location_1"] | df["location_2"])==True]
y = y[(y["location_1"] & y["location_2"])==False]