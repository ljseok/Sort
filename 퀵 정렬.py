array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 한개일 경우 종료
        return
    pivot = start # 첫번째 원소 = 피벗
    left = start + 1
    right = end

    while left<=right: # 엇갈릴때 까지 반복
        while left <= end and array[left] <= array[pivot]: # 피벗보다 큰 데이터를 찾을 때 까지 반복
            left+=1
        while right > start and array[right] >= array[pivot]: # 피벗보다 작은 데이터를 찾을 때 까지 반복
            right-=1
        if left > right: # 엇갈렸을때
            array[right], array[pivot] = array[pivot], array[right] #작은 데이터와 피벗 교체
        else: # 엇갈리지 않았으면
            array[left], array[right] = array[right], array[left] #작은 데이터와 큰 데이터 교체
    quick_sort(array,start,right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


