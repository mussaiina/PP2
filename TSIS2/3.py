
arr = list(map(int, input().split()))


cnt = 0
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if arr[i] == arr[j] and i < j:
            cnt += 1

print(cnt)