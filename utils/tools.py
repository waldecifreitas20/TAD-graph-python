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


def sortEdgesByWeight(edges=[]) -> list:
    sorting = edges.copy()
    for l, edge1 in enumerate(edges):
        for c, edge2 in enumerate(edges):

            if sorting[l].weight < sorting[c].weight:
                sorting[l], sorting[c] = sorting[c], sorting[l] 
    return sorting


