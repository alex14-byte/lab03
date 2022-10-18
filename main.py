import random
from random import randint
n = int(input())

mas = [input() for i in range(n)]
for i in range(n):
    print(mas[i], sep="")
print("   ")
for i in range(n - 1):
    for j in range(n - 2, i - 1, -1):
        if mas[j + 1] < mas[j]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]
for i in range(n):
    print(mas[i], sep="")