# Autor: Renée Richter
# Datum: 01.12.2024
# Zweck: AOC day 1 juhuuu es geht los

import re

# -------------------------
# read in

l1 = []
l2 = []
line = None
with open("input.txt", "r") as datei:
    while True:
        line = datei.readline()
        if line == "":
            break
        matches = re.findall("[0-9]+", line)
        l1.append(int(matches[0]))
        l2.append(int(matches[1]))

l1.sort()
l2.sort()

# -------------------------
# Part 1

erg = 0
for i in range(len(l1)):
    erg += abs(l1[i] - l2[i])

print("The answer for Part 1 is:", erg)

# -------------------------
# Part 2

erg2 = 0

str2 = ""
for e in l2:
    str2 += str(e) + " "

for i in range(len(l1)):
    fa = len(re.findall(str(l1[i]), str2))
    erg2 += l1[i] * fa

print("The answer for Part 2 is:", erg2)
