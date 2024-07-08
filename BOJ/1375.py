import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N,M = map(int,input().split())
compare = defaultdict(list)
for i in range(M):
    x, y = input().split()
    compare[y].append(x)

def bfs(x):
    que = deque()
    que.append(x)

    a, vis = list(), defaultdict(int)
    while que:
        q = que.popleft()
        a.append(q)
        
        for c in compare[q]:
            if not vis[c]:
                que.append(c)
                vis[c] = 1
    return a

answer = list()
for _ in range(int(input())):
    x, y = input().split()
    if x == y:
        answer.append('gg')
    elif y in bfs(x):
        answer.append(y)
    elif x in bfs(y):
        answer.append(x)
    else:
        answer.append('gg')
print(' '.join(answer))