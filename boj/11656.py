

from cProfile import label


n = int(input())

student = []

for i in range(n):
    [a,b,c,d] = map(str,input().split())
    student.append([a,int(b),int(c),int(d)])


sorted_student = sorted(student, key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in sorted_student:
    print(i[0])