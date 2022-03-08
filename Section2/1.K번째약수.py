'''
자연수 p, q
if p를 q로 나누었을때 나머지가 0 이면 q는 p의 약수

N의 약수 중 K번째 작은 수 출력하기
ex) 1,2,3,6 이니까 6의 약수중 3번째작은수 3 출력하기
만약 못찾으면 -1
'''
import sys
sys.stdin = open("input_1.txt", "rt")

n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
