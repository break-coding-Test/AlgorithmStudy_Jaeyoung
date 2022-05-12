
n, m = map(int,input().split())


dd = set()
bb = set()


for i in range(n):
    dd.add(input())
    
    
for i in range(m):
    bb.add(input())
    
arr = sorted(list(dd & bb))

print(len(arr))

for i in arr:
    print(i)

