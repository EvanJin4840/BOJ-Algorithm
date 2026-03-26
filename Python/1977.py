import math

M = int(input())
N = int(input())

total = 0
numbers = []
flag = False

for i in range(1, 101, 1):
    if i * i >= M and i * i <= N:
        total += i * i
        numbers.append(i * i)
        flag = True

if flag == False:
    print(-1)
else:
    print(total)
    print(min(numbers))