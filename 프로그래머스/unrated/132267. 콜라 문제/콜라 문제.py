def solution(a, b, n):
    sumValue = 0
    while n >= a:

        c = n // a * b  #
        n = n // a * b + (n % a)
        sumValue += c
    return sumValue
