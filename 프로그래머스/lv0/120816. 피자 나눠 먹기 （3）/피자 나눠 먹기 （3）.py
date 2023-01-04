def solution(slice, n):
    if n % slice == 0:
        return n // slice
    elif n < slice:
        return int(n / slice)
    elif n > slice:
        return int(n / slice) +1