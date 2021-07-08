n = int(input())
my_dict = {}
for i in range(n):
    k, v = input().split()
    my_dict[k] = v

s = input()
keys = list(my_dict.keys())
values = list(my_dict.values())

if s in values:
    print(keys[values.index(s)])
else:
    print(my_dict[s])