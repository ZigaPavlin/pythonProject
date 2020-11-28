def pivot_array(array, pivot):
    n = len(array)
    arr2 = array[:]

    # arr2 = array

    for i in range(n):
        arr2[i] = array[(i - pivot) % n]

    return arr2


def binary_search(array, findme):
    print('input a sorted array')
    n2 = len(array)
    n0 = 0
    n1 = int((n2 + n0) / 2)

    while (n2 - n0) > 1:
        print(n2, n1)
        if findme == array[n1]:
            return True, n1
        elif findme > array[n1]:
            n2 = n2
            n0 = n1
            n1 = int((n2 + n0 - 1) / 2)
        else:
            n2 = n1
            n0 = n0
            n1 = int((n2 + n0 + 1) / 2)

    return False, -1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 19, 39, 199, 123]
    arr2 = pivot_array(arr, 3)
    print(arr)
    print(arr2)

    find = 1
    print(binary_search(arr, find))

    if arr[binary_search(arr, find)[0]]:
        print(arr[binary_search(arr, find)[1]])

    for i in range(len(arr)):
        print(i, arr, pivot_array(arr, i))
