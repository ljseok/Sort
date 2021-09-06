array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min = i # 가장 작은 원소

    for j in range(i+1, len(array)):
        if array[min] > array[j]:
            min = j
        array[i], array[min] = array[min], array[i] # swap

print(array)