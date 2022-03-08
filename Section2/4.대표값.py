'''
N명의 학생 수학성적의 평균구하기(소수첫째자리반올림)
평균과 가장 가까운 학생의 번호 출력하기
(답이 2개일 경우 성적이 높은 학생의 번호 출력, 만약 점수 여러개면 번호 빠른 학생꺼 출력)
'''

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