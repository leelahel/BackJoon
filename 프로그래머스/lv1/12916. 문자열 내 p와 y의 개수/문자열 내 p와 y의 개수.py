def solution(s):
    # 문자열 s에서 'p'와 'y'의 개수를 세기 위해 변수 초기화
    p_count = 0
    y_count = 0

    # 문자열 s를 반복하면서 'p'와 'y'의 개수를 센다
    for char in s:
        if char.lower() == 'p':  # 대소문자 구분 없이 'p'를 찾음
            p_count += 1
        elif char.lower() == 'y':  # 대소문자 구분 없이 'y'를 찾음
            y_count += 1

    # 'p'와 'y'의 개수 비교
    if p_count == y_count:
        return True
    else:
        return False
