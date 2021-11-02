# By Aleksey (sorta)
# This is the starter code given by the challenge that was buggy.
# I couldn't work out the bug, so I just ran it and got partial credit :P

def caesarBoxCipherEncoding2(inputString):

    def encode(s, n):
        res = []
        for i in range(n):
            for j in range(len(s) // n):
                res.append(s[j * n + i])
        return ''.join(res)

    res = 0
    length = len(inputString)
    sqrt_length = int(math.sqrt(length))
    for n in range(2, sqrt_length + 1):
        if length % n == 0:
            if encode(encode(inputString, n), n) == inputString:
                res += 2

    if sqrt_length ** 2 == length:
        res += 1

    return res
