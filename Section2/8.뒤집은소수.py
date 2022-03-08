'''
N개 자연수입력되면 각 자연수 뒤집고 그 뒤집은 수가 소수이면 그 수를 출력

뒤집기 함수 : def reverse(x)
소수 판단 : def isPrime(x)
'''

import sys
sys.stdin = open("input_8.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

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
        print(tmp, end=" ")
