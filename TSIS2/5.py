n = int(input())

product = 1
sum = 0
while n != 0:
    product *= n % 10
    sum += n % 10
    n //= 10
print(product - sum)