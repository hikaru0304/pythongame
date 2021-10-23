# 1.길이가 n개인 리스트의 요소(element/item)들을 0으로 초기화하기
n = 7
result1 = [0] * n
print(result1)

result2 = [0 for x in range(n)]
print(result2)
# 2.원소의 갯수를 카운터하기
# ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2의 갯수를 카운팅
arr = [1,2,2,3,1,1,3,2]
# count 변수를 0으로 초기화
count = 0
# arr의 모든 요소들에 대해서:
for x in arr:
# 각각의 원소가 2이면:
    if x == 2:
        pass
# count에 1을 증가

# 3.range를 이용하여 1부터 7까지 출력하는 코드를 최대한 여러가지로 표현해보기
# ex) N부터 M까지의 숫자를 출력하는 print_range(N, M) 함수를 정의하기
