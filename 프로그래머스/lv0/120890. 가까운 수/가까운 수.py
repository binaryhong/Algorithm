def solution(array, n):
    array.append(n)
    sortedArray = sorted(array)
    if n == sortedArray[-1]:
        return sortedArray[sortedArray.index(n)-1]
    if n == sortedArray[0]:
        return n
    if n - sortedArray[sortedArray.index(n)-1] > sortedArray[sortedArray.index(n)+1] - n:
        return sortedArray[sortedArray.index(n)+1]
    else:
        return sortedArray[sortedArray.index(n)-1]