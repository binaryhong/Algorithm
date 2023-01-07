def solution(n):
    k = 10000
    a = [False, False] + [True] * (k - 1)
    primes = []
    answer = []
    result = []

    for i in range(2, k + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, k + 1, i):
                a[j] = False
                
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)

    for value in result:
        if value in primes:
            answer.append(value)
            
    return answer