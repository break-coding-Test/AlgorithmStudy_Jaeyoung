

n = int(input())

pos = []

for i in range(n):
    [posx,posy] = map(int,input().split())
    pos.append([posx,posy])
    

for i in sorted(pos,key=lambda x : (x[1],x[0])):
    print(i[0],i[1], sep=" ")