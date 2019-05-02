def pow(x, n): # O(log(n))
    res = 1
    while n > 0:
        if n & 1:
            res *= x
        x = x * x
        n = n // 2
    return res

def gcd(a, b): # O(log(a + b))
    while b > 0:
        r = a % b
        a = b
        b = r
    return a