

n = int(input())

arr = []
for i in range(n):
    arr.append(str(input()))

#set으로 리스트 중복 제거    
set_arr = set(arr)

#list로 다시 리스트로 만들기
arr = list(set_arr)

# 먼저 사전순으로 정렬
arr.sort()

# 길이순으로 정렬
arr.sort(key = len)

for i in arr:
    print(i)