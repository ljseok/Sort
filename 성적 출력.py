n = int(input())
arr = []

for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))
arr = sorted(arr, key=lambda st:st[1])

for st in arr:
    print(st[0], end= ' ')