import sys
N, K = map(int,input().split())

checkpoints = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

dist = 0
while checkpoints and checkpoints[-1]>=0:
    dist += 2*checkpoints[-1]
    for i in range(K):
        if checkpoints and checkpoints[-1]>=0:
            checkpoints.pop()

checkpoints.reverse()

while checkpoints:
    dist -= 2*checkpoints[-1]
    for i in range(K):
        if checkpoints:
            checkpoints.pop()

print(dist)