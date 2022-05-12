

n = int(input())

arr = []

for i in range(n):
    [n,m] = input().split()
    arr.append([n,m])
    
arr.sort(key= lambda x : x[1])

for i in arr:
    print(i[0])