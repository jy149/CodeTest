'''
정 N면체, 정 M면체 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램
여러개일 경우 오름차순
N, M 은 4, 6, 8, 12, 20 중 하나
'''
import sys
sys.stdin = open("input_5.txt","rt")

n,m = map(int, input().split())

# 처음 초기화 리스트 만들기
cnt = [0]*(n + m + 1)

# 주사위 두 개 던졌을때 경우의 수
for i in range(1, n+1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

# 가장 작은값 초기화
max = -2147000000

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

# 정답 출력하기
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=" ")
