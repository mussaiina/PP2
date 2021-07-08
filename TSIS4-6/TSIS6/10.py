
mylist = list(map(int, input().split()))
even = []
for i in mylist:
    if i % 2 == 0:
        even.append(i)
print(*even)