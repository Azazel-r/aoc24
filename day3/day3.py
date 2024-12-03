# Autor: René Richter
# Datum: 03.12.2024
# Zweck: AoC 2024 Day 3 hab heute ne payday 2 heist tabelle aufgestellt und plane das
#        als datenbank für nen heist-dle zu machen juhu

import re

# -------------------------
# read in

string = ""
with open("input.txt", "r") as datei:
    while True:
        line = datei.readline()
        if line == "":
            break
        string += line

# -------------------------
# Part 1

mults = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", string)

erg = 0
for i in range(len(mults)):
    erg += mult(mults[i])

print(erg)

# -------------------------
# Part 2

erg2 = 0
mults2 = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", string)
enabled = True
for i in range(len(mults2)):
    if mults2[i] == "do()":
        enabled = True
    elif mults2[i] == "don't()":
        enabled = False
    else:
        if enabled:
            erg2 += mult(mults2[i])

print(erg2)

# -------------------------
# used classes & functions

def mult(s):
    nums = re.findall("[0-9]{1,3}", s)
    return int(nums[0]) * int(nums[1])
