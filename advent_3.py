# -*- coding: utf-8 -*-

import pandas as pd


df = pd.read_csv("data_day3.txt", names = ["map"])
df["position0"] = df.index + 1 #R1 D1
df["position1"] = df.index*3 + 1 #R3 D1
df["position2"] = df.index*5 + 1 #R5 D1
df["position3"] = df.index*7 + 1 #R7 D1
#Remove first lane
df_part1 = df[1::]

length_of_pattern = len(df_part1["map"][1])
df_part1["tree0"] = df_part1.apply(lambda x: (True if x["map"][(x["position0"]%length_of_pattern)-1] == "#" else False), axis = 1)
df_part1["tree1"] = df_part1.apply(lambda x: (True if x["map"][(x["position1"]%length_of_pattern)-1] == "#" else False), axis = 1)
df_part1["tree2"] = df_part1.apply(lambda x: (True if x["map"][(x["position2"]%length_of_pattern)-1] == "#" else False), axis = 1)
df_part1["tree3"] = df_part1.apply(lambda x: (True if x["map"][(x["position3"]%length_of_pattern)-1] == "#" else False), axis = 1)

#part 1
tree1 = df_part1[df_part1["tree1"]==True]

#part 2
tree0 = df_part1[df_part1["tree0"]==True]
tree2 = df_part1[df_part1["tree2"]==True]
tree3 = df_part1[df_part1["tree3"]==True]

df_part2 = df[::2].reset_index() #d2
df_part2["position"] = df_part2.index + 1 #R1
#Remove first lane
df_part2 = df_part2[1::]
length_of_pattern = len(df_part2["map"][2])
df_part2["tree"] = df_part2.apply(lambda x: (True if x["map"][(x["position"]%length_of_pattern)-1] == "#" else False), axis = 1)

tree = df_part2[df_part2["tree"]==True]

#multiply number of values from tree, tree0 - tree3 for answer