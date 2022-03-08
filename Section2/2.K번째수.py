import sys
sys.stdin = open("input_2.txt", "rt")

# test case 읽기
T = int(input())

for t in range(T):
    # case별 첫번째 줄 읽기
    n, s, e, k = map(int, input().split())

    # 다음 줄 리스트 읽기
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" % (t+1, a[k-1]))
