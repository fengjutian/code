# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        position = i
        temp_value = arr[i]
        while position > 0 and arr[position - 1] > temp_value:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = temp_value


list = [4, 5, 6, 2, 3, 1]
insertion_sort(list)
print(list)

