# PROBLEM 5

found = False
i = 1

while not found:
    if i%1000000 == 0:
        print(i)
    if i%20 == 0 and i%19 == 0 and i%18 == 0 and i%17 == 0 and i%16 == 0 and i%15 == 0 and i%14 == 0 and i%13 == 0 and i%12 == 0 and i%11 == 0 and i%10 == 0 and i%9 == 0 and i%8 == 0 and i%7 == 0 and i%6 == 0 and i%5 == 0 and i%4 == 0 and i%3 == 0 and i%2 == 0 and i%1 == 0:
        print("The smallest number divisable by 1 to 20 is:", i)
        found = True

    i += 1