# PROBLEM 2

fibSeq = [1, 1]
while fibSeq[len(fibSeq)-1] < 4000000:
    fibSeq.append(fibSeq[len(fibSeq)-1] + fibSeq[len(fibSeq)-2])

totEven = 0
for i in fibSeq:
    if i%2 == 0 and i < 4000000:
        totEven += i

print("Total of even fibonacci numbers:", totEven)
