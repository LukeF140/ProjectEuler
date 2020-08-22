# PROBLEM 4

larPal = 0

found = False
for i in range (999, 99, -1):
    for n in range(999, 99, -1):
        mul = i*n
        if str(mul) == ''.join(reversed(str(mul))):
            if mul > larPal:
                larPal = mul

print("Largest palindrome from the product of two 3-digit numbers:", str(larPal))
