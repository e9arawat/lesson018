""" The purpose of this lesson today is to write as many functions as we can in the best way we can.
    All numbers must be formatted in lacs (00,00,000) and crores (00,00,00,000)
    Precision to two decimal places is required. Round any additional precision to two decimal places."""
def round_off(num):
    return round(num, 2)

def formatting(num):
    first, second, size = num, '', len(num)
    if '.' in num:
        first, second, size = num[:-3], num[-3:], size-3
    index = 3
    while index < len(first):
        first = first[:-index] + ',' + first[-index:]
        index += 3
    return first+second

def simple_interest(principal, term, rate):
    ans = (principal * term * rate)
    ans += principal 
    ans = formatting(str(round_off(ans)))
    return ans
    
def compound_interest(principal, term, rate, n:int=1):
    ans = principal*((1+(rate/n))**(n*term))
    ans = formatting(str(round_off(ans)))
    return ans

def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True, n: int=1):
    for _ in range(0,term):
        if not end_of_period:
            principal += payment
        ans = principal * rate
        if end_of_period:
            principal += payment
        principal += ans
    ans = principal
    ans = formatting(str(round_off(ans)))
    return ans
import math
def savings_calculator(present_value, future_value, term, rate, end_of_period=True, n: int=1):
    if not end_of_period:
        rate = rate / (1+rate)
    ans = (future_value - present_value * (1 + rate) ** term) / ((1 + rate) ** term - 1)
    ans = math.ceil(ans * 100)/100
    ans = formatting(str(round_off(ans)))
    return ans 

if __name__ == "__main__":
    print(simple_interest(123456, 23, 0.08))
    print(compound_interest(123456, 23, 0.08))
    print(compound_interest_with_payments(0, 368970.52, 35, 0.10))
    print(savings_calculator(0, 1e8, 35, 0.10))
