N,M,K,S = map(int,input().split())
items = set(input().split())
loads = set([input().replace(' ','') for l in range(M)])
villages = {'1'}

switch = True
while switch:
    switch = False
    for l in loads.copy():
        if set(l[0:2])&villages and set(l[4:])<=items:
            villages = set(l[0:2])|villages
            items.add(l[2])
            loads.remove(l)
            switch = True

print(len(villages))

#print(f"현재길:{l} 조건 {bool(set(l[0:2])&villages)} {set(l[4:])<items}  남은길:{loads} item:{items} 마을:{villages}")