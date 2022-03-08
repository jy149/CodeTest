'''
자연수 N이 입력되면 소수가 몇개인지 출력하는 문제
'''
import sys
sys.stdin = open("input_7.txt","rt")

n = int(input())

# 리스트 초기화
ch = [0] * (n+1)
cnt = 0

for i in range(2,n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)

