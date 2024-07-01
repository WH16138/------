n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

totalcost = 0
mincost = cost[0]
for i in range(n-1):
    mincost = min(mincost, cost[i])
    totalcost += mincost*dist[i]

print(totalcost)