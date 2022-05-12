
n = int(input())

arr = []

for i in range(n):
    [age,name] = map(str,input().split())
    arr.append([int(age),name])
    

for p in sorted(arr,key=lambda x: (x[0])):
    
    print(p[0],p[1],sep=" ")