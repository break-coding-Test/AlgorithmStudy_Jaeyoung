

num = list(input())
num.sort(reverse=True)
is_zero = False
sum = 0

for i in num:
    sum += int(i)
    if int(i) == 0:
        is_zero = True

if(sum % 3 != 0 or not(is_zero)):
    print(-1)
else :
    print("".join(num))
    
    
    