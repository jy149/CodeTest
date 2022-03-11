'''
오름차순 정렬된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램

sort() 함수로 돌면 nlogn 로 돌음. 근데 n번만에 돌릴수도있음
각 읽어들인 리스트의 index들 간의 비교를 통해서 새로운 리스트에 append하는 방식으로..!
'''
import sys
sys.stdin = open("input_4.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 포인트변수 초기화
p1 = p2 = 0

c = []

# 둘 중 하나가 아무거나 처리할때까지,
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end=" ")




