

n = int(input())

pos = []
for i in range(n):
    
    # 좌표, 색깔
    [x,color] = map(int,input().split())
    pos.append([x,color])

pos.sort(key= lambda x : (x[1],x[0]))

sum = 0

for i in range(1,len(pos) - 1):
    a = i - 1
    b = i + 1
    if(pos[a][1] == pos[b][1]):
        if(abs(pos[a][0] - pos[i][0]) > abs(pos[b][0] - pos[i][0])):
            sum += abs(pos[b][0] - pos[i][0])
        else:
            sum += abs(pos[a][0] - pos[i][0])
    else:
        if(pos[i][1] == pos[a][1]):
            sum += abs(pos[a][0] - pos[i][0])
        else:
            sum += abs(pos[b][0] - pos[i][0])
        
    
sum += abs(pos[n-1][0] - pos[n-2][0]) + abs(pos[0][0] - pos[1][0])
print(sum)