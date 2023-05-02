import numpy as np
m = 10
n = 14
v = 0.3
q = 1/n
mas = np.random.randint(0, 100, size=(n, m))
print(mas)
print('Критерий Ходжа-Лемана')
e = []
for i in mas:
    mine = min(i)
    sum = 0
    for j in i:
        sum += j*q
    e.append(v*sum+(1-v)*mine)
print(e)
print('res:', e.index(max(e))+1)
print('Критерий Байеса-Лапласа')
eq = []
sum = 0
for _ in mas:
    for j in _:
        sum += j*q
    eq.append(sum)
    sum = 0
print(q)
print(eq)
print('res: ', eq.index(max(eq))+1)
