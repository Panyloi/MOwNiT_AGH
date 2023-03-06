import numpy as np
import matplotlib.pyplot as plt

# zad 1 
# rng = np.random.default_rng()
# x = rng.random(dtype=np.float32)
# openCV
x = 0.22664672136306763
print(x)
n = 10**7
a = np.full(n, x, dtype=np.float32)

# print(a.sum())
a_sum = a.sum()

acc = 0.0

for i in range(n):
    acc += a[i]

# print(acc)

# zad 2
# błąd bezwzględny

bb = np.absolute(a_sum - acc)
bw = bb / a_sum

print(f'blad bezwzgledny {bb}, blad wzgledny {bw}')

