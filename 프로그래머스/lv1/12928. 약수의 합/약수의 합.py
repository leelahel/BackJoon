def solution(n):
    total_sum = 0  # 약수의 총합을 저장할 변수 초기화
    
    for i in range(1, n+1):  # 1부터 n까지 반복
        if n % i == 0:  # n을 i로 나누었을 때 나머지가 0인 경우는 i가 n의 약수
            total_sum += i  # 약수를 총합에 더함
    
    return total_sum  # 약수의 총합 반환
