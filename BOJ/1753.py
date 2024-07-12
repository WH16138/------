import sys, heapq, math
input = sys.stdin.readline

V, E = map(int,input().split())
S = int(input())

graph = [[] for _ in range(V+1)] # 이중 리스트 : i 번째 노드에서 접근가능한 다른 노드를 리스트 형태로 저장

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v, w)) # 단방향 그래프로 업데이트

def dijkstra(start):
    dist = [math.inf] * (V+1) # 시작점으로부터 모든 정점으로의 거리 (무한으로 초기화)
    dist[start] = 0 # 자기 자신으로의 거리는 0
    que = [(0, start)]
    
    while que:
        cur_dist, cur_node = heapq.heappop(que) #우선순위 큐 자료구조 사용
        
        if cur_dist <= dist[cur_node]:continue # 최단경로 이외의 경로는 건너뜀
        
        for next_node, weight in graph[cur_node]: # 현재 노드에서 접근가능한 모든 노드를 불러옴
            next_dist = cur_dist + weight
            if next_dist < dist[next_node]: # 더 빠른 경로가 가능한 경우 거리 업데이트 && 다른 경로에 재활용하기 위해 우선순위 큐에 저장
                dist[next_node] = next_dist
                heapq.heappush(que, (next_dist, next_node))

    return dist

dist = dijkstra(S)

for i in range(1, V+1):
    if math.isinf(dist[i]):
        print("INF")
    else:
        print(dist[i])