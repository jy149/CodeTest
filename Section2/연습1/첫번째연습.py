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

print()
print()

# 6. 자릿수의 합
import sys
sys.stdin = open("input_6.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
'''
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
'''

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -float("inf")
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

print()
print()

# 7. 소수 (에라토스테네스 체)
import sys
sys.stdin = open("input_7.txt", "rt")

n = int(input())

ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)


# 8. 뒤집은 소수
import sys
sys.stdin = open("input_8.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

# 수 뒤집는 함수
def reverse(x):
    res = 0
    while x > 0 :
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

# 소수확인 함수
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end =" ")


print()
print()


# 9. 주사위 게임
import sys
sys.stdin = open("input_9.txt", "rt")
n = int(input())

max_price = -float("inf")

for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[2] and a[1] == a[2]:
       price = 10000 + a[0] * 1000
    elif a[0] == a[1] or a[0] == a[2]:
        price = 1000 + a[0]*100
    elif a[1] == a[2]:
        price = 1000 + a[1] * 100
    else:
        price = a[2] * 100
    if price > max_price:
        max_price = price

print(max_price)


# 10. 점수계산
import sys
sys.stdin = open("input_10.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)


































