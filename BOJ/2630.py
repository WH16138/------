n = int(input()) # n 입력
grid = [[] for i in range(n)] # 종이를 저장할 리스트 선언

for i in range(n):
    grid[i] = list(map(int, input().split())) # n개의 라인을 입력받아 값을 리스트 형태로 저장

white = 0 #흰색 종이 개수 
blue = 0 #파란색 종이 개수
def solve(x,y,d):
    global white, blue # 전역변수 처럼 사용
    if d == 1: # 종이의 크기가 1일 경우 처리
        if grid[x][y]:
            blue += 1
        else:
            white += 1
        return
    
    # 그 외
    target = grid[x][y] # 첫번째 부분의 종이색
    for i in range(d):
        for j in range(d):
            if grid[x+i][y+j]!=target: # 완전탐색 과정에서 다른 색이 발견되면 종이를 4등분
                solve(x,y,d//2) # 왼쪽 상단
                solve(x+d//2,y,d//2) # 오른쪽 상단
                solve(x,y+d//2,d//2) # 왼쪽 하단
                solve(x+d//2,y+d//2,d//2) # 오른쪽 하단
                return
    if target: # 완전탐색 결과 색이 일치할때 결과 처리
        blue +=1
    else:
        white +=1

solve(0,0,n) # 코드 실행

print(f"{white}\n{blue}") # 형식에 맞게 결과 출력