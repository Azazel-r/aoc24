# Autor: Renée Richter
# Datum: 07.12.2024 (leider)
# Zweck: Verspäteter AOC day6 whatever man i can do this

# -------------------------
# used classes & functions

import re
import time
from copy import deepcopy

def turnLeft(field): # unused
    n = len(field)
    for row in field:
        row.reverse()
    for i in range(n):
        for j in range(i + 1, n):
            field[i][j], field[j][i] = field[j][i], field[i][j]

def turnRight(field): # unused
    for i in range(3):
        turnLeft(field)

def nextDir(direction):
    # girl writes worst one liner in history, asked to leave coding competition
    return (1,0) if direction == (0,-1) else (0,1) if direction == (1,0) else (-1,0) if direction == (0,1) else (0,-1) if direction == (-1,0) else None

def outside(position, l):
    return position[0] < 0 or position[1] < 0 or position[0] >= l or position[1] >= l

def printfield(field):
    for row in field:
        print(" ".join(row))
        
def makeString(p,d):
    return str(p[0]) + ',' + str(p[1]) + 'w' + str(d[0]) + ',' + str(d[1])

def loops(field, pos, obj):
    if pos == obj or field[obj[1]][obj[0]] == "#":
        return False
    
    direction = (0,-1)
    field[obj[1]][obj[0]] = "#"
    logs = makeString(pos,direction) + " "
    
    while True:
        nxt = (pos[0] + direction[0], pos[1] + direction[1])
        if outside(nxt, len(field)):
            field[obj[1]][obj[0]] = "."
            return False
        
        elif field[nxt[1]][nxt[0]] == ".":
            pos = nxt
            string = makeString(pos, direction)
            if re.search(string, logs) != None:
                field[obj[1]][obj[0]] = "."
                return True
            logs += string + " "

        elif field[nxt[1]][nxt[0]] == "#":
            direction = nextDir(direction)
            string = makeString(pos, direction)
            if re.search(string, logs) != None:
                field[obj[1]][obj[0]] = "."
                return True
            logs += string + " "

def loops2(obj, pos, bound): # electric boogaloo
    direction = (0,-1)
    logs = " " + makeString(pos, direction) + " "
    while True:
        nxt = (pos[0] + direction[0], pos[1] + direction[1])
        isObstacle = re.search(" "+str(nxt[0])+','+str(nxt[1])+" ", obj) != None

        if outside(nxt, bound):
            return False
        
        elif not isObstacle:
            pos = nxt
            posStr = makeString(pos, direction)
            if re.search(" "+posStr+" ", logs) != None:
                return True
            logs += posStr + " "

        elif isObstacle:
            direction = nextDir(direction)
            posStr = makeString(pos, direction)
            if re.search(" "+posStr+" ", logs) != None:
                return True
            logs += posStr + " "
            
# -------------------------
# read in

startpos = ()
lines_ = []
direction = (0,-1)
fieldstr = ""
with open('input.txt', 'r') as datei:
    count = 0
    while True:
        line = datei.readline()
        if line == "":
            break
        lines_.append(list(line[:-1]))
        find = re.search('\^', line)
        if find != None:
            startpos = (find.start(), count)
        count += 1

# -------------------------
# Part 1

tryoutpos= []
erg = 0
pos = startpos
lines = deepcopy(lines_)
while True:
    nxt = (pos[0] + direction[0], pos[1] + direction[1])
    if outside(nxt, len(lines)):
        erg += 1
        lines[pos[1]][pos[0]] = "X"
        break
    elif lines[nxt[1]][nxt[0]] == ".":
        lines[pos[1]][pos[0]] = "X"
        lines[nxt[1]][nxt[0]] = "^"
        pos = nxt
        tryoutpos.append(pos)
        erg += 1
    elif lines[nxt[1]][nxt[0]] == "X":
        lines[pos[1]][pos[0]] = "X"
        lines[nxt[1]][nxt[0]] = "^"
        pos = nxt
    elif lines[nxt[1]][nxt[0]] == "#":
        direction = nextDir(direction)
    #print("--------------")
    #printfield(lines)

print(erg)

# -------------------------
# Part 2 (new readin dont ask why)
# really shitty but it works trust me and it only takes like 15mins lol

objCoords = " "
length = 0
with open('input.txt', 'r') as datei:
    y = 0
    while True:
        line = datei.readline()
        if line == "":
            break
        allhashtags = re.finditer("#", line[:-1])
        for find in allhashtags:
            objCoords += str(find.start()) + ',' + str(y) + " "
        y += 1
    length = y

erg2 = 0
stime = time.perf_counter()
"""
for i in range(length):
    print("row", i, "done at:", round(time.perf_counter()-stime,2))
    for j in range(length):
        objPos = (i,j)
        objStr = str(objPos[0])+','+str(objPos[1])
        valid = objPos != startpos and re.search(objStr, objCoords) == None
        if valid and loops2(objCoords + " " + objStr, (startpos[0], startpos[1]), length):
            erg2 += 1
"""
#print(tryoutpos)
i = 0
for posi in tryoutpos:
    if i % 100 == 0:
        print(i, "out of", erg, "done at", time.perf_counter() - stime)
    objStr = str(posi[0])+','+str(posi[1])
    if loops2(objCoords + " " + objStr + " ", (startpos[0], startpos[1]), length):
        erg2 += 1
    i += 1

print(erg2)

# -------------------------
# Failed attempt at Part 2
# WARNING; SUPER SLOW LOL takes like an hour or something and is wrong

"""
erg2 = 0
pos = startpos
lines = deepcopy(lines_)
lines[pos[1]][pos[0]] = "."
for i in range(len(lines[0])):
    #print("i:", i, "/ 130")
    for j in range(len(lines)):
        if loops(lines, pos, (i,j)):
            erg2 += 1
            print(i, j, "ist richtig")
print(erg2)
"""
