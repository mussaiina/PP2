f = open('input.txt', 'r')
n = int(input())
lines = []
cnt = 0
for line in f:
    cnt += 1
    lines.append(line)
for i in range(cnt - n, cnt):
    print(lines[i])