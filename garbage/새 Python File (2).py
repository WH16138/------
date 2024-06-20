O = list(input())
N = list(input())

dist = 0
while 1:
    while len(O) and len(N) and O[-1] == N[-1]:
        O.pop()
        N.pop()
        print(''.join(O),'|', ''.join(N),dist)
    if len(O) and len(N) and O[-1]!= N[-1]:
        dist += 1
        while len(O) and len(N) and O[-1] != N[-1]:
            N.pop()
            print(''.join(O),'|', ''.join(N),dist)
    if len(O) == 0:
        if len(N):
            print(dist+1)
        else:
            print(dist)
        break
    elif len(N) == 0:
        print(-1)
        break