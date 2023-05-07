# import math
# from math import pow as m

print('A B C')
for A in range(2):
    for B in range(2):
        for C in range(2):
            f = ((A and B and (not C)) or not(A) or not(B) or C)
            if f:
                print(A, B, C, f)

