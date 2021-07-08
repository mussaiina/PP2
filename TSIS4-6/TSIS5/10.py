with open('input.txt', 'r') as f:
    txt = f.read().split()
dict = {}
n = 0
for i in txt:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict.items())