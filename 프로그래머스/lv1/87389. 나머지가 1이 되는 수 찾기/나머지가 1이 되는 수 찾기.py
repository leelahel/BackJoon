def solution(n):
    x = 1  # x의 초기값을 1로 설정
    
    while n % x != 1:  # n을 x로 나눈 나머지가 1이 아닌 경우 반복
        x += 1  # x 값을 1씩 증가
    
    return x  # 가장 작은 x 값 반환

    return answer