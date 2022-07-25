
def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    return arr



if __name__ == '__main__':

    arr = [8,4,23,42,16,15]
    arr_2 = [20,18,12,8,5,-2]
    arr_3 = [5,12,7,5,5,7]
    arr_4 = [2,3,5,7,13,11]

    insertion_sort(arr)
    print(arr)