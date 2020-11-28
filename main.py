def pivot_array(array, pivot):
    n = len(array)
    arr2 = array[:]

    for i in range(n):
        arr2[i] = array[(i - pivot) % n]

    return arr2


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5]
    arr2 = pivot_array(arr, 3)
    print(arr)
    print(arr2)

    for i in range(len(arr)):
        print(i, pivot_array(arr, i))
