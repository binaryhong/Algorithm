def generate_sequences(N, M, numbers):
    numbers.sort()  # 수를 정렬하여 중복 처리 및 사전 순 정렬
    used = [False] * N  # 숫자 사용 여부 추적

    def backtrack(sequence):
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
            return
        prev = -1  # 이전 숫자 추적 변수
        for i in range(N):
            if not used[i] and numbers[i] != prev:
                used[i] = True
                sequence.append(numbers[i])
                backtrack(sequence)
                used[i] = False
                sequence.pop()
                prev = numbers[i]  # 이전 숫자를 현재 숫자로 업데이트

    backtrack([])

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
generate_sequences(N, M, numbers)