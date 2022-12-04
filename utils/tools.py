def indexOfMaxValue(iterable):
    maxNumber = max(iterable)
    index = iterable.index(maxNumber)
    return index


def sortIndexesOfMaxValue(iterable=list, reverse=False):
    sortedList = []
    length = len(iterable)
    _iterable = iterable.copy()

    while length > len(sortedList):
        biggest = indexOfMaxValue(_iterable)
        sortedList.append(biggest)
        _iterable[biggest] = -10000000000000
    
    if reverse:  
        sortedList.reverse()
    return sortedList


def sortEdgesByWeight(edges=[], reverse=False) -> list:
    sorting = edges.copy()
    for l, edge1 in enumerate(edges):
        for c, edge2 in enumerate(edges):

            if sorting[l].weight < sorting[c].weight:
                sorting[l], sorting[c] = sorting[c], sorting[l] 
    if reverse:
        sorting.reverse()
    return sorting


def indexOfMin(iterable=[]):
    smaller = iterable[0]
    index = 0
   
    for i, item in enumerate(iterable):
        if item > smaller:
            smaller = item
            index = i 
    return index
