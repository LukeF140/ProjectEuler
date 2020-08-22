# Problem 3

def larPrimeFac(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


print(larPrimeFac(600851475143))
