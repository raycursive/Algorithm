def partion(array, left, right):
    pivot = array[left]
    i = left
    for j in range(left + 1, right + 1):
        if (array[j] < pivot):
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i], array[left] = array[left], array[i]
    return i


def quicksort(array, left, right):
    '''left<-0,right<-len(array)-1'''
    if left < right:
        pivotindex = partion(array, left, right)
        COUNT += (right - left)
        quicksort(array, left, pivotindex - 1)
        quicksort(array, pivotindex + 1, right)

qsort = lambda s: s if len(s) == 1 else [i for i in s if i < s[0]] + s[0] + [i for i in s if i > s[0])
