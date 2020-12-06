# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd

def conditon_1(x, delimeter = '|'):
    length = len(x.split(delimeter))
    if length == 8:
        return True
    elif "cid" not in x and length == 7:
        return True
    else:
        return False
    
def check_byr(x):
    if "byr" in x:
        data = x.split("byr:")[1].split('|')[0]
        if int(data) > 1919 and int(data) < 2003:
            return True
        else:
            return False
    else:
        return False

def check_iyr(x):
    if "iyr" in x:
        data = x.split("iyr:")[1].split('|')[0]
        if int(data) > 2009 and int(data) < 2021:
            return True
        else:
            return False
    else:
        return False

def check_eyr(x):
    if "eyr" in x:
        data = x.split("eyr:")[1].split('|')[0]
        if int(data) > 2019 and int(data) < 2031:
            return True
        else:
            return False
    else:
        return False

def check_hgt(x):
    if "hgt" in x:
        data = x.split("hgt:")[1].split('|')[0]
        if "cm" in data:
            height = int(data.strip("cm"))
            if height >149 and height < 194:
                return True
            else:
                return False
            
        elif "in" in data:
            height = int(data.strip("in"))
            if height >58 and height < 77:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def check_hcl(x):
    #this can be done using regex but i am not proficient in it and lazy to look it up
    set_allowed = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if "hcl" in x:
        data = x.split("hcl:")[1].split('|')[0]
        if data[0] == "#":
            data = data[1::]
            if len(data) == 6:
                for i in data:
                    if i in set_allowed:
                        continue
                    else:
                        return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def check_ecl(x):
    if "ecl" in x:
        data = x.split("ecl:")[1].split('|')[0]
        if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        else:
            return False
    else:
        return False

def check_pid(x):
    if "pid" in x:
        data = x.split("pid:")[1].split('|')[0]
        if len(data) == 9:
            try:
                int(data)
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return False
    
with open('data_day4.txt') as f:
    data_list = []
    tmp = []
    for line in f:
        if line == '\n':
            data_list.append(' '.join(tmp).replace('\n', ' ').split(' '))
            tmp = []
        else:
            tmp.append(line)
    data_list.append(' '.join(tmp).replace('\n', ' ').split(' '))

data_list = ['|'.join(filter(lambda x: x!= '', data)) for data in data_list]

df = pd.DataFrame(data_list, columns= ["data"])
df["fields"] = df["data"].apply(lambda x: '|'.join([i.split(':')[0] for i in x.split('|')]))
df["valid_1"] = df["fields"].apply(conditon_1)

#Part 1 
valid = df[df["valid_1"]==True]
not_valid = df[df["valid_1"]==False]

df["byr"] = df["data"].apply(check_byr)
df["iyr"] = df["data"].apply(check_iyr)
df["eyr"] = df["data"].apply(check_eyr)
df["hgt"] = df["data"].apply(check_hgt)
df["hcl"] = df["data"].apply(check_hcl)
df["ecl"] = df["data"].apply(check_ecl)
df["pid"] = df["data"].apply(check_pid)
#part2 answer
valid_2 = df[df["byr"] & df["iyr"] & df["eyr"] & df["hgt"] & df["hcl"] & df["ecl"] & df["pid"]]