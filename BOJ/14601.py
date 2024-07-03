k = int(input()) # k를 입력받음
hole = tuple(map(int,input().split())) # 구멍 위치를 입력받음
hole = (hole[0]-1, (2**k)-hole[1]) # 구멍 위치의 리스트상 인덱스 값

grid = [[-1]*(2**k) for i in range(2**k)] # 2차원 리스트 생성

count = 0 # 타일 번호
def solve(x,y,n,h):# 시작점 x,y | 크기 n | 구멍위치 h
    global count # 전역변수 처럼 사용
    if n == 2: # 면적이 4인 경우
        count += 1
        for dx,dy in ((0,0),(1,0),(0,1),(1,1)):
            if (x+dx,y+dy) != h: # 구멍을 제외하고 타일 설치
                grid[y+dy][x+dx] = count
    else:
        m = n//2 
        count += 1
        num = count
        # 바닥을 4등분 한 뒤, 
        # 구멍이 위치한 구역은 구멍 위치를 유지,
        # 구멍이 위치하지 않은 나머지 3개 구역에 걸쳐 ㄱ 타일을 설치하고 
        # 구멍이 생긴 것처럼 처리하여 재귀적으로 작동
        for X,Y,H in [(x,y,(x+m-1,y+m-1)),(x+m,y,(x+m,y+m-1)),(x,y+m,(x+m-1,y+m)),(x+m,y+m,(x+m,y+m))]:
            if X<=h[0]<X+m and Y<=h[1]<Y+m: # 구멍이 있는 구역
                solve(X,Y,m,h)
            else: # 없는 구역
                grid[H[1]][H[0]] = num # 없는 구역에 타일이 한칸 걸쳐지도록 설치후, 이것을 구멍으로 처리 
                solve(X,Y,m,H)

solve(0,0,2**k,hole) # 코드 실행

for line in grid: # 정답 출력
    print(' '.join(map(str,line)))