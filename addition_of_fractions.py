def solution(numer1, denom1, numer2, denom2):
    answer = [numer1*denom2 + numer2*denom1, denom1*denom2]
    gcd = GCD(answer[0], answer[1])

    return [answer[0]//gcd, answer[1]//gcd]
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

solution(9,2,1,3) # [5,6]
