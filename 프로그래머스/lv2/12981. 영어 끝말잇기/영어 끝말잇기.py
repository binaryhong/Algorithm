def solution(n, words):
    stack = [words[0]]
    for i in range(1, len(words)):
        # stack의 마지막 원소의 마지막 문자가 현재 words의 첫번째 문자와 같고,
        # word가 stack 없을경우
        if stack[-1][-1] == words[i][0] and words[i] not in stack:
            stack.append(words[i])
            # print("stack:", stack)
        else:
            return [i % n + 1, i // n + 1]  # 번호, 차례 
    return [0, 0]