def partition(arrNames,arrSize, left, right):
    i = left
    j = right - 1
    pivot = arrSize[right]
    while i < j:
        while i < right and arrSize[i] < pivot:
            i += 1
        while j > left and arrSize[j] >= pivot:
            j -= 1
        if i < j:
            arrSize[i], arrSize[j] = arrSize[j], arrSize[i]
            arrNames[i], arrNames[j] = arrNames[j], arrNames[i]
    if arrSize[i] > pivot:
        arrSize[i], arrSize[right] = arrSize[right], arrSize[i]
        arrNames[i], arrNames[right] = arrNames[right], arrNames[i]            

    return i

def quickSort(arrNames,arrSize, left, right):
    if left < right:
        partition_pos = partition(arrNames,arrSize, left, right)
        quickSort(arrNames,arrSize,left,partition_pos - 1)
        quickSort(arrNames,arrSize,partition_pos + 1,right)
