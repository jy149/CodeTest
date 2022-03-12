import sys

# 1. 회문 문자열 검사

sys.stdin = open("input_1.txt", "rt")
n = int(input())
for i in range(n):
    string = input()
    string2 = string.upper()
    if string2 == string2[::-1]:
        print("#{} {}".format(i+1, "YES"))
    else:
        print("#{} {}".format(i + 1, "NO"))

print()
print()

sys.stdin = open("input_1.txt", "rt")
n = int(input())
for i in range(n):
    string = input()
    string2 = string.upper()
    for j in range(n//2):
        if string2[j] != string2[-1-j]:
            print("#{} {}".format(i + 1, "NO"))
            break
    else:
        print("#{} {}".format(i + 1, "YES"))

print()
print()

# 2.숫자만 출력
sys.stdin = open("input_2.txt", "rt")
string = input()

res = 0
for i in string:
    if i.isdecimal():
        res = res*10 + int(i)

print(res)

cnt = 0
for i in range(1,res+1):
    if res % i == 0:
        cnt+= 1

print(cnt)

print()
print()

# 3. 카드 역백치 (정올기출)
sys.stdin = open("input_3.txt", "rt")
chk = [i for i in range(21)]

for _ in range(10):
    s, e = map(int,input().split())
    for i in range((e-s+1)//2):
        chk[s+i], chk[e-i] = chk[e-i], chk[s+i]
chk.pop(0)
for x in chk:
    print(x, end=" ")

print()
print()


# 4. 두 리스트 합치기
sys.stdin = open("input_4.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
res = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        res.append(a[p1])
        p1 += 1
    else:
        res.append(b[p2])
        p2 += 1
if p1 < n:
    res = res + a[p1:]
if p2 < m:
    res = res + b[p2:]

for x in res:
    print(x, end = " ")

print()
print()

# 5. 수들의 합
sys.stdin = open("input_5.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1

tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)

print()
print()

# 6.격자판 최대 합
sys.stdin = open("input_6.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = - float("inf")

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum3 = sum4 = 0
for i in range(n):
    sum3 += a[i][i]
    sum4 += a[i][n-i-1]
if sum3 > largest:
    largest = sum3
if sum4 > largest:
    largest = sum4

print(largest)

print()
print()

# 7. 사과나무 (다이아몬드)
sys.stdin = open("input_7.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

tot = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        tot += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(tot)
