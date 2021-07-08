m, n = map(int, input().split())
s1 = set()
s2 = set()
for i in range(m):
    s1.add(int(input()))
for i in range(n):
    s2.add(int(input()))

both = s1.intersection(s2)
s1.symmetric_difference_update(both)
s2.symmetric_difference_update(both)

print(len(both))
print(*sorted(both, key=int))
print(len(s1))
print(*sorted(s1, key=int))
print(len(s2))
print(*sorted(s2, key=int))