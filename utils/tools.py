def indexOfMaxValue(iterable):
    maxNumber = max(iterable)
    index = iterable.index(maxNumber)
    return index

def sortIndexesOfMaxValue(iterable=list):
    sortedList = []
    length = len(iterable)
    _iterable = iterable.copy()

    while length > len(sortedList):
        biggest = indexOfMaxValue(_iterable)
        sortedList.append(biggest)
        _iterable[biggest] = -10000000000000

    return sortedList

