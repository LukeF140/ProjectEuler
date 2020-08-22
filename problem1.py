# PROBLEM 1

tot = 0
for i in range(1,1000):
    if i%3 == 0:
        tot += i
    elif i%5 == 0:
        tot += i

print("Sum of all intagers that are multiples of 3 or 5", str(tot))
        
