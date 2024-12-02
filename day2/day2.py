# Autor: René Richter
# Datum: 02.12.2024
# Zweck: AoC day 2 hab heute schon balatro gespielt auf green stake und gewonnen
# TRIGGER WARNING WORST CODE EVER

import re

class Zahlenreihe:

    def __init__(self, a, goingup):
        self.zahlen1 = [a]
        self.zahlen2 = [a]
        self.up = goingup
        self.ignore = True
        self.alive = [True, True]

    def compare(self, a, b):
        return not ((self.up and (a >= b or b-a > 3)) or (not self.up and(a <= b or a-b > 3)))

    def add(self, b) -> bool:
        if self.ignore:
            a = self.zahlen1[-1]
            if not self.compare(a,b):
                self.ignore = False
                if len(self.zahlen1) > 1:
                    a_ = self.zahlen1[-2]
                    if self.compare(a_,b):
                        self.zahlen2.pop()
                        self.zahlen2.append(b)
                    else:
                        self.alive[1] = False
                else:
                    self.zahlen2.pop()
                    self.zahlen2.append(b)
                return True
            self.zahlen1.append(b)
            self.zahlen2.append(b)
            return True
        else:
            a1 = self.zahlen1[-1]
            a2 = self.zahlen2[-1]
            if self.alive[0]:
                if self.up and (a1 >= b or b-a1 > 3):
                    self.alive[0] = False
                elif not self.up and (a1 <= b or a1-b > 3):
                    self.alive[0] = False
                else:
                    self.zahlen1.append(b)
            if self.alive[1]:
                if self.up and (a2 >= b or b-a2 > 3):
                    self.alive[1] = False
                elif not self.up and (a2 <= b or a2-b > 3):
                    self.alive[1] = False
                else:
                    self.zahlen2.append(b)
                    
            return self.alive[0] or self.alive[1]
                                

def getUp(line):
    ups = 0
    downs = 0
    for i in range(len(line)-1):
        if int(line[i]) < int(line[i+1]):
            ups += 1
        else:
            downs += 1
    return ups > downs

l = []
with open("input.txt", "r") as datei:
    while True:
        line = datei.readline()
        if line == "":
            break
        l.append(line[:-1].split(" "))

erg = 0
for i in range(len(l)):
    safe = True
    up = True
    tolerance = True
    for j in range(len(l[i])-1):
        a = int(l[i][j])
        b = int(l[i][j+1])
        if j == 0 and a > int(l[i][-1]):
            up = False
        if up and (a >= b or b-a > 3):
            safe = False
        elif not up and (a <= b or a-b > 3):
            safe = False
    if safe:
        erg += 1

# Part 1
print(erg)

erg2 = 0
for i in range(len(l)):
    #print("")
    #print("--------------------------")
    #print("Zeile", i)
    z = Zahlenreihe(int(l[i][0]), getUp(l[i]))
    safe = True
    for j in range(1,len(l[i])):
        if not z.add(int(l[i][j])):
            safe = False
            break
    if safe:
        #print("yearg is good")
        erg2 += 1
    else:
        #print("NOPERS its bad")
        pass

# Part 2
print(erg2)
