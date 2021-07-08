def Divisors(n):
    divs = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def Sum(*divs):
    x = 0
    for i in divs:
        x += i
    return x


n = int(input())
divs = Divisors(n)
if n == Sum(*divs):
    print(n, "is perfect")
else:
    print("no")