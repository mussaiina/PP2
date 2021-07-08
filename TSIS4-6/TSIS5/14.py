a = open('colors.txt', 'r')
b = open('signs.txt', 'r')
for x in a:
    print(x + b.readline(), sep='\n', end='')