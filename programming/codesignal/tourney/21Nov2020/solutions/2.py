# By Aleksey (sorta)
# This is starter code where I just modified the "return False" part in line 7 :P

def isLuckyNumber(n):
    while n > 0:
        tmpDigit = n % 10
        if tmpDigit != 7 and tmpDigit != 4:
            return False
        n = n // 10
    return True
