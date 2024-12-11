# Autor: René Richter
# Datum: 04.12.2024
# Zweck: AoC 2024 Day 4; Hab gestern Pilze genommmen und wooow es war super

import re
  
# -------------------------
# classes & functions used

def getDiagonalLine(arr, x):
    erg1 = ""
    erg2 = ""
    y = 0
    newx = x
    if x >= len(arr[0]):
        newx = len(arr[0])-1
        y = x - newx
    for i in range(min(len(arr)-y,newx+1)):
        erg1 += arr[y+i][-1-newx+i]
        erg2 += arr[y+i][newx-i]
    return erg1, erg2
      
def getSubList(arr, x, y):
    return arr[y][x:x+3] + arr[y+1][x:x+3] + arr[y+2][x:x+3]

def matchIt(s):
    return re.match("M.M.A.S.S$|M.S.A.M.S$|S.S.A.M.M$|S.M.A.S.M$", s) != None

# -------------------------
# read in

lines = []
with open("input.txt", "r") as datei:
    while True:
        line = datei.readline()
        if (line == ""):
            break
        lines.append(line[:-1])

# -------------------------
# Part 1 (way too complicated) (not really but kinda)

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
    result = getDiagonalLine(lines, i)
    linesDiag1.append(result[0])
    linesDiag2.append(result[1])

hzt, vtc, diag1, diag2 = 0, 0, 0, 0

for i in range(len(lines)):
    hzt += len(re.findall(r"XMAS", lines[i])) + len(re.findall(r"SAMX", lines[i]))
    vtc += len(re.findall(r"XMAS", linesRot[i]))+ len(re.findall(r"SAMX", linesRot[i]))
    
for i in range(len(linesDiag1)):
    diag1 += len(re.findall(r"XMAS", linesDiag1[i])) + len(re.findall(r"SAMX", linesDiag1[i]))
    diag2 += len(re.findall(r"XMAS", linesDiag2[i])) + len(re.findall(r"SAMX", linesDiag2[i]))

#print (hzt, vtc, diag1, diag2)
print("The answer for Part 1 is:", hzt+vtc+diag1+diag2)
# i didnt use a singular variable as the sum for debug purposes

#print(len(lines) == len(linesRot)) # True
#print(len(linesDiag1) == len(linesDiag2)) # True

# -------------------------
# Part 2 (somehow easier)

erg2 = 0
for y in range(len(lines)-2):
    for x in range(len(lines[0])-2):
        s = getSubList(lines, x, y)
        if matchIt(s):
            erg2 += 1

print("The answer for Part 2 is:", erg2)
