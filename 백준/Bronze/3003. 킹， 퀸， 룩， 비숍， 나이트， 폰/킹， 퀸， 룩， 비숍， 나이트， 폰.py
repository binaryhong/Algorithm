num_list = list(map(int, input().split()))


def solution(s):
    chess = [1, 1, 2, 2, 2, 8]
    result = []

    for i in range(len(chess)):
        print(chess[i] - s[i], end=" ")
solution(num_list)