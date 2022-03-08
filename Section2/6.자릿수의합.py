'''
N개의 자연수 입력, 각 자연수의 자릿수 합구하고 그 합이 최대인 자연수 출력
def digit_sum(x) 활용
'''
import sys
sys.stdin = open("input_6.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
'''
# 첫번째 방법 각 자릿수합
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
'''
# 두번째 방법 각 자릿수 합
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