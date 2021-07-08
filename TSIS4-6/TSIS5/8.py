with open('input.txt', 'r') as txt:
    words = txt.read().split()
max = 0
for x in words:
    if len(x) > max:
        max = len(x)
        s = x
print(s)
