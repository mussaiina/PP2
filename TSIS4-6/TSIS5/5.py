f = open('input.txt', 'r')
x = []
for line in f:
    x.append(line)
print(*x)