# Autor: Renée Richter
# Datum: 11.12.2024
# Zweck: Niemals im leben schaff ich es noch hinterherzukommen, danke mathe breakdown gestern

import re

# -------------------------
# used functions & classes

def binaryList(x : int, length : int) -> list:
    return list(map(int, list(format(x,f'0{length}b'))))

def ternaryList(x : int, length: int) -> list:
    if x == 0:
        return [0 for i in range(length)]
    nums = []
    while x:
        x, r = divmod(x, 3)
        nums.append(str(r))
    return list(map(int, list(''.join(reversed(nums)).zfill(length))))
    

def findout(n, l, ops = 0):
    while True:
        opsList = binaryList(ops, len(l)-1)
        erg = l[0]
        for i in range(len(opsList)):
            op = opsList[i]
            if not op:
                erg += l[i+1]
            elif op:
                erg *= l[i+1]
                
        if sum(opsList) == len(opsList) and erg != n:
            return -1
        elif erg != n:
            ops += 1
            continue
        return n

def findout2(n, l, ops = 0):
    while True:
        opsList = ternaryList(ops, len(l)-1)
        erg = l[0]
        for i in range(len(opsList)):
            op = opsList[i]
            if op == 0:
                erg += l[i+1]
            elif op == 1:
                erg *= l[i+1]
            elif op == 2:
                erg = int(str(erg) + str(l[i+1]))
                
        if sum(opsList) == 2 * len(opsList) and erg != n:
            return -1
        elif erg != n:
            ops += 1
            continue
        return n

# -------------------------
# read in

lines = []
with open("input.txt", "r") as datei:
    while True:
        line = datei.readline()[:-1]
        if line == "":
            break
        matches = list(map(int, re.findall('\d+', line)))
        lines.append(matches)


# -------------------------
# Part 1 & 2 :3 (takes a bit but dw its fine)

erg = 0
erg2 = 0
for row in lines:
    find = findout(row[0], row[1:])
    erg += find if find >= 0 else 0
    
    find = findout2(row[0], row[1:])
    erg2 += find if find >= 0 else 0
    
print(erg)
print(erg2)
