N,K = map(int,input().split())
coin = [int(input())for _ in range(N)] # n개의 줄을 입력받아 리스트에 정수형으로 저장

count = 0
while K: # 잔돈이 0이 될때까지
    if coin[-1]<=K: # 모든 동전이 배수 관계이므로, 가능한 가장 큰 단위부터 사용 
        count+=K//coin[-1]
        K%=coin[-1]
    else:coin.pop() #남은 돈 보다 동전의 가치가 클 경우 동전 제거
print(count)