'''
문자와 숫자 섞여있는 문자열 중 숫자만 추출하여 순서대로 자연수 만들기,
만들어진 자연수와 그 자연수의 약수 갯수 출력
'''
import sys
sys.stdin = open("input_2.txt", "rt")

s = input()

res = 0

for x in s:
    # .isdigit -> 숫자형태 다 찾기, .isdecimal() -> 0~9 숫자찾기
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

# 약수의 갯수
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)

