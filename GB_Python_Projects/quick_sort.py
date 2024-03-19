def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        greater = [item for item in array[1:] if item > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)