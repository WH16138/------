import math as m
n = int(input())

pos = []
for i in range(n):
    pos.append(list(map(int,input().split())))

dist = []
for i in range(n):
    for j in range(n):
        if i != j:
            dist.append(m.dist(pos[i],pos[j]))