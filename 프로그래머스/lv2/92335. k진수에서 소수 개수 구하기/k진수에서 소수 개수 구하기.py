def solution(n, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                return False
        return True

    def count_primes(s):
        cnt = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if '0' not in s[i:j]:
                    if is_prime(int(s[i:j])):
                        if (i == 0 or s[i-1] == '0') and (j == len(s) or s[j] == '0'):
                            cnt += 1
        return cnt

    converted = ''
    while n > 0:
        n, mod = divmod(n, k)
        converted += str(mod)
    converted = converted[::-1]

    return count_primes(converted)