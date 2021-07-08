letters = [' ']
for i in range(26):
    letters.append(chr(i+65))
s = input().upper()

for i in s:
    if i not in letters:
        print("Not pangram")
        exit()
    else:
        continue
print("Pangram")