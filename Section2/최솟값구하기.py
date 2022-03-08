arr = [5, 3, 7, 9, 2, 5, 2, 6]

# 가장 작은 변수를 출력하기 위한 변수 설정

# 가장 큰 값으로 초기화
arrMin = float('inf')

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)