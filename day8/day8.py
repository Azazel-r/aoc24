# Autor: Renée Richter
# Datum: 11.12.2024
# Zweck: vielleicht brech ich die uni ab man. ich bin nicht dafür gemacht

import re

# -------------------------
# used classes & functions

def antiInField(a, b, bound):
    vec = (b[0]-a[0], b[1]-a[1])
    antinode = (b[0]+vec[0], b[1]+vec[1])
    ret = 0 <= antinode[0] <= bound and 0 <= antinode[1] <= bound and not antinode in antilocs
    if ret:
        #print(b[0]+vec[0], b[1]+vec[1])
        antilocs.append(antinode)
    return ret

def getAntinodeCount(a, b, bound):
    ret = 0
    vec = (b[0]-a[0], b[1]-a[1])
    anti1 = b
    anti2 = a
    while True:
        val1 = 0 <= anti1[0] <= bound and 0 <= anti1[1] <= bound
        val2 = 0 <= anti2[0] <= bound and 0 <= anti2[1] <= bound
        if val1:
            if not anti1 in antilocs:
                ret += 1
                antilocs.append(anti1)
            anti1 = (anti1[0]+vec[0], anti1[1]+vec[1])
        elif val2:
            if not anti2 in antilocs:
                ret += 1
                antilocs.append(anti2)
            anti2 = (anti2[0]-vec[0], anti2[1]-vec[1])
        else:
            break
    return ret

# -------------------------
# read in

locs = " "
y = 0
antilocs = []
with open('input.txt', 'r') as datei:
    while True:
        line = datei.readline()[:-1]
        if line == "":
            break
        matches = re.finditer("[^\.]", line)
        for match in matches:
            locs += match.group() + '|' + str(match.start()) + ',' + str(y) + " "
        y += 1

# -------------------------
# Part 1

erg = 0
# worst one line list declare in history ([A-Z][a-z][0-9] alle dabei)
symbols = [chr(i) for i in range(65,91,1)] + [chr(i) for i in range(97,123,1)] + [i for i in range(10)]

for sym in symbols:
    matches = list(re.finditer(f"{sym}\|(\d+,\d+)", locs))
    groups = [match.group(1) for match in matches]
    for i in range(len(groups)):
        a = tuple(map(int, groups[i].split(',')))
        for j in range(i+1, len(groups)):
            b = tuple(map(int, groups[j].split(',')))
            erg += 1 if antiInField(a,b,y-1) else 0
            erg += 1 if antiInField(b,a,y-1) else 0

print(erg)

# -------------------------
# Part 2

antilocs = []
erg2 = 0
for sym in symbols:
    matches = list(re.finditer(f"{sym}\|(\d+,\d+)", locs))
    groups = [match.group(1) for match in matches]
    for i in range(len(groups)):
        a = tuple(map(int, groups[i].split(',')))
        for j in range(i+1, len(groups)):
            b = tuple(map(int, groups[j].split(',')))
            erg2 += getAntinodeCount(a,b,y-1)

print(erg2)
