n = int(input())
dist = list(map(int,input().split())) # 거리를 정수형으로 리스트에 저장
cost = list(map(int,input().split())) # 가격을 정수형으로 리스트에 저장

totalcost = 0 # 최종 가격
mincost = cost[0] # 현재까지 주유소의 최소가격, 시작가격은 첫 주유소 가격
for i in range(n-1): # 0 부터 n-1 번째 도로 까지
    mincost = min(mincost, cost[i]) # i 번째 주유소와 현재까지의 최저가를 비교
    totalcost += mincost*dist[i] # 최저가를 이용하여 i 번째 도로 주행

print(totalcost)