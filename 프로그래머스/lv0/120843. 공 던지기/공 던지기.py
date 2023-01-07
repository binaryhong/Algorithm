def solution(numbers, k):
    new_list = []
    if len(numbers) % 2 == 0:
        for i in range(0,max(numbers)+1):
            if i % 2 == 1:
                new_list.append(i)
        new_list = new_list * k
        return new_list[k - 1]
    else:
        new_list = numbers * k
        return new_list[2*k-2]