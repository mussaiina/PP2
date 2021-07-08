nums = list(map(int, input().split()))
min = 1000
for i in nums:
    if i < min and i > 0:
        min = i
print(min)