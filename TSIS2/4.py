gain = list(map(int, input().split()))
max = 0
order = 0
for i in range(0, len(gain)):
    if order + gain[i] > max:
        max = order + gain[i]
    order += gain[i]
print(max)