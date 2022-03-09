# 1번문제 K번째 약수
import sys
sys.stdin = open("input_1.txt", "rt")
n, k = map(int, input().split())
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

print()
print()

# 2번문제 K번째 수
import sys
sys.stdin = open("input_2.txt", "rt")

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#{} {}".format(t+1, a[k-1]))

print()
print()

# 3번문제 K번째 큰 수
import sys
sys.stdin = open("input_3.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            s.add(a[i]+a[j]+a[z])

res = list(s)
res.sort(reverse = True)
print(res[k-1])

print()
print()

# 4번문제 대표값
import sys
sys.stdin = open("input_4.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

# 평균구하기
ave = round(sum(a)/n)

# 최솟값을 넣을 값 최대값으로 초기화
min = float("inf")

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)


print()
print()

# 문제 5번 정다면체
import sys
sys.stdin = open("input_5.txt", "rt")

n, m = map(int, input().split())

cnt = [0] *(n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i + j] += 1
print(cnt)

max = -float("inf")

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end = " ")









































