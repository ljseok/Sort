'''
n,k = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
'''

n = 5
k = 3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

a.sort() # a에 대해서 오름차순으로 정렬
b.sort(reverse=True) #b에 대해서 내림차순으로 정렬

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # 원소교체
    else:
        break

print(sum(a))