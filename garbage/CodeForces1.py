n, q = map(int,input().split())

tower1 = list(map(int,input().split()))
power1 = list(map(int,input().split()))
pipe1 = list(map(int,input().split()))

for i in range(q):
    update = list(map(int,input().split()))
    tower1[update[0]-1] = update[1]
    power1[update[0]-1] = update[2]
    if update[0] != n:pipe1[update[0]-1] = update[3]
    wine = 0

    tower = tower1.copy()
    power = power1.copy()
    pipe = pipe1.copy()

    for i in range(n):
        convert = min(tower[i],power[i])
        tower[i] = tower[i] - convert
        wine += convert
        if i != n-1:
            flow = min(tower[i],pipe[i])
            tower[i] = tower[i] - flow
            tower[i+1] = tower[i+1] + flow

    print(wine)