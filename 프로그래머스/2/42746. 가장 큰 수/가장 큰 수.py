def solution(numbers):
    newNumberList = [str(num) for num in numbers]
    # 핵심: 문자열을 3번 반복해서 비교 (999, 343434, 303030 ...)
    newNumberList.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(newNumberList)
    # 000...0 같은 케이스 처리
    return '0' if answer[0] == '0' else answer