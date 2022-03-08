import sys
sys.stdin = open("input_9.txt", "rt")

n = int(input())

res = -float("inf")

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 100 + (b * 100)
    else:
        money = c * 100

    if money > res:
        res = money
print(res)