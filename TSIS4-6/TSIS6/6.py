n = int(input())
a, b = map(int, input().split())
if n in range(a, b):
    print("yes")
else:
    print('No')