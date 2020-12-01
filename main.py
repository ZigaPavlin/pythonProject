def pivot_array(array, pivot):
    n = len(array)
    arr2 = array[:]

    # arr2 = array

    for i in range(n):
        arr2[i] = array[(i - pivot) % n]

    return arr2


def binary_search(array, findme):
    print('input a sorted array')
    n2 = len(array)-1
    n0 = 0
    n1 = int((n2 + n0) / 2)

    while (n2 - n0) > 1:
        print(n2, n1, n0)
        if findme == array[n1]:
            return True, n1
        elif findme > array[n1]:
            n2 = n2
            n0 = n1
            n1 = int((n2 + n0) / 2)
        else:
            n2 = n1
            n0 = n0
            n1 = int((n2 + n0) / 2)

    if findme == array[n2]:
        return True, n2

    if findme == array[n0]:
        return True, n0

    return False, -1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 19, 39, 199, 123]
    arr.sort()

    find = 199
    print(binary_search(arr, find))


