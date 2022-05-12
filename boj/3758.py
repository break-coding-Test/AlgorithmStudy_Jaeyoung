

import functools


def comp(x,y):
    #만약에 길이가 다르다면
    if(len(x) != len(y)):
        min_num = min(len(x),len(y))
        
        for i in range(0,min_num):
            
            if(x[i] != y[i]):
                
                #x[i]가 더 큰 숫자이면
                if(x[i] > y[i]):
                    # x를 앞으로 이동
                    return -1
                elif(x[i] < y[i]):
                    #y[i] 가 더 큰 숫자이면
                    # y를 앞으로 이동
                    return 1
        #만약에 다 비교했는데 min_num까지 숫자가 동일하면 
        #길이가 긴 것을 반환한다.
        if(len(x) > len(y)):
            return -1
        else:
            return 1
    #비교하는 두 문자열이 길이가 같은 경우
    else:
        # 사전순으로 큰값이 숫자가 큰 수다
        if(x > y):
            return -1
        else:
            return 1
            
        
n = int(input())

arr = []
for i in range(n):
    arr.append(str(input()))

arr.sort(key=functools.cmp_to_key(comp))

print(" ")
for i in arr:
    print(i)