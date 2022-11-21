A = 9
B = A
C = A
B = float(B)
C = str(C)
print(A, B, C)
print(id(A), id(B), id(C))

D = 1
F = str(1)
F = int(F)
print(D, F)
print(id(D), id(F))
