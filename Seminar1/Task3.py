from math import sqrt

n = int(input("Введите число: "))
while n>100000 or n<0:
    n = int(input("Введите число: "))
i = 2
while i <= sqrt(n):
    if n % i == 0:
        print("Составное число")
        break
    i += 1
else:
    print("Простое число")


def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    if n > 1:
        return True


a = int(input("Второй способ. Введите число: "))

if is_prime(a):
    print("Простое число")
else:
    print("Составное число")