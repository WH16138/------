import sys

N = input()
time = [list(map(int,x.strip().split())) for x in sys.stdin.read().splitlines()] # n개의 줄을 입력받음
time.sort(key=lambda x:(x[1],x[0])) # 회의가 끝나는 시간이 빠른 순으로 정렬

now = 0 # 현재시간 or 이전 회의의 종료시간
answer = 0
for t in time: 
    if t[0] >= now: # 시간이 겹치지 않고, 최대한 빨리 끝나는 회의를 배정하는 과정을 반복
        answer += 1
        now = t[1]

print(answer) # 정답 출력