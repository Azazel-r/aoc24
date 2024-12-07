# Autor: René Richter
# Datum: 07.12.2024 (leider)
# Zweck: 2 tage zu spät aber here we go. AoC24 day fiiive bitches

import re

# -------------------------
# classes & functions used

def check(a,b):
    return re.search(f"{a}\|{b}", rules) != None

def makeRight(l):
    while True:
        breakup = False
        for i in range(-1, -len(l)-1, -1):
            a = l[i]
            for j in range(-1, i, -1):
                b = l[j]
                if check(b, a):
                    l.insert(len(l)+j+1, a)
                    l.pop(l.index(a))
                    breakup = True
                    break
            if breakup:
                break
        if not breakup:
            return l

# -------------------------
# read in

rules = ","
lines = []
truelines = []

with open("input.txt", 'r') as datei:
    while True:
        line = datei.readline()
        if line == "\n":
            break
        rules += line[:-1] + ","

    while True:
        line = datei.readline()
        if line == "":
            break
        lines.append(list(map(lambda x : int(x), line[:-1].split(','))))
        truelines.append(True)

# -------------------------
# Part 1

erg = 0
for i in range(len(lines)):
    breakup = False
    for j in range(-1, -len(lines[i])-1, -1):
        obj = lines[i][j]
        for k in range(j, 0, 1):
            if check(lines[i][k], obj):
                breakup = True
                truelines[i] = False
                break
        if breakup:
            break
    if not breakup:
        erg += lines[i][int(len(lines[i])/2)]

print(erg)

# -------------------------
# Part 2

erg2 = 0
for i in range(len(lines)):
    if not truelines[i]:
        line = makeRight(lines[i])
        erg2 += line[int(len(line)/2)]

print (erg2)
