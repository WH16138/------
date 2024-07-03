N = int(input())
t = sorted(list(map(int,input().split())), reverse=1) #소요시간을 입력받고, 오래걸리는 순서로 정렬
print(sum([t[i]*(i+1) for i in range(N)])) # (가장 오래걸리는 시간 x 1 + ... + 가장 빠른 시간 x n) 출력