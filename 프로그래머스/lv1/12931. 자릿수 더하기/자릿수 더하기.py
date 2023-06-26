def solution(N):
    # 정수 N을 문자열로 변환하여 각 자릿수에 접근할 수 있도록 함
    digits = str(N)
    
    # 각 자릿수의 합을 저장할 변수 초기화
    digit_sum = 0
    
    # 각 자릿수를 순회하며 합을 계산
    for digit in digits:
        digit_sum += int(digit)
    
    return digit_sum
