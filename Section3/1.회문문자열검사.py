'''
N개의 문자열 데이터를 받아 읽을때 앞으로 읽으나 뒤로읽으나 같으면 '회문문자열'
만약 회문문자열이면 'YES'출력, 아니면 'NO'출력
(대소문자 구별 X)
'''
import sys
sys.stdin = open("input_1.txt", "rt")

n = int(input())
'''
for i in range(n):
    s = input()
    # 들어오면 다 대문자화
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#{} NO".format(i+1))
            break
    else:
        print("#{} YES".format(i+1))
'''

# 더 짧은 코드
# s[::-1] 하면 전체를 읽는데 -1 로 거꾸로 읽음
for i in range(n):
    s = input()
    # 들어오면 다 대문자화
    s = s.upper()
    if s == s[::-1]:
        print("#{} YES".format(i + 1))
    else:
        print("#{} NO".format(i + 1))
