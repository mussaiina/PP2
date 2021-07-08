import string
n = int(input())
with open('letters.txt', 'w') as f:
    letters = string.ascii_uppercase
    order = [letters[i:i+n] + '\n' for i in range(0, len(letters), n)]
    f.writelines(order)