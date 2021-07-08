zero = list(map(int, input().split()))
cnt = 0
for i in zero:
    if i == 0:
        cnt += 1
    else:
        print(i, end=' ')
for i in range(cnt):
    print(0, end=' ')