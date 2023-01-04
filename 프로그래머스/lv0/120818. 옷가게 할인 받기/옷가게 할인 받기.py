def solution(price):
    if 100000 <= price < 300000:
        rate = 0.05
    elif 300000<= price < 500000:
        rate = 0.10
    elif 500000<= price:
        rate = 0.20
    else:
        rate = 0.00
        
    return int(price*(1-rate))