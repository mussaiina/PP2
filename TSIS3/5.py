arr = list(map(int, input().split()))
k = int(input()) % len(arr)
if k > 0:
    a = int(len(arr) - k)
    arr = arr[a:] + arr[:a]
else:
    arr = arr[-k:] + arr[:-k]

print(*arr, end=' ')