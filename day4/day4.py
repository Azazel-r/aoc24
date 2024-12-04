# Autor: René Richter
# Datum: 04.12.2024
# Zweck: AoC 2024 Day 4; Hab gestern Pilze genommmen und wooow es war super

# -------------------------
# read in

lines = []
with open("input.txt", "r") as datei:
    line = datei.readline()
    if (line == ""):
        break
    lines.append(line)

# -------------------------
# Part 1

linesRot = []
for i in range(len(lines[0])):
    temp = ""
    for j in range(len(lines)):
        temp += lines[j][i]
    linesRot.append(temp)

linesDiag1 = []
linesDiag2 = []
l = len(lines) + len(lines[0]) - 1

for i in range(l):
    l2 = min(i, len(lines[0]-1))


def getDiagonalLine(arr, num):
    
