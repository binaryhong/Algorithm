def solution(n):
    ans = 1
    while n > 2:
        if n % 2 == 0:
            n //=2
        elif n % 2 !=0:
            n -=1
            ans +=1
            
    return ans