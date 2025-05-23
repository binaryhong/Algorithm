def solution(numbers, target):
    # 경우의 수를 세는 함수 정의
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 합이 target과 같으면 경우의 수 1개 추가
            if current_sum == target:
                return 1
            # 아니면 0개
            else:
                return 0

        # 현재 숫자에 +를 붙이는 경우
        # print("plus index+1:", index+1, "current_sum:", current_sum, "numbers[index]:", numbers[index])
        plus = dfs(index + 1, current_sum + numbers[index])
        # print("plus:", plus)
        # 현재 숫자에 -를 붙이는 경우
        # print("minus index+1:", index+1, "current_sum:", current_sum, "numbers[index]:", numbers[index])
        minus = dfs(index + 1, current_sum - numbers[index])
        # print("minus:", minus)
        # 두 경우의 수를 합쳐서 반환
        return plus + minus

    # dfs 탐색 시작 (처음에는 0번째 숫자, 합은 0)
    answer = dfs(0, 0)
    return answer
