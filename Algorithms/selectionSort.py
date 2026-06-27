# the selection sort tracks the min value

array = [1,6,9,3,5,2,8,4,7]


def selectionSort(array):
    for i in range(len(array)):
        min = i # initialize the min index to the current index
        for j in range(i+1,len(array)):
            if array[j] < array[min]: # if we found a new min value, update the min index
                min = j

        array[i], array[min] = array[min], array[i] # swapping the min value with the current index value



selectionSort(array) # call the function to sort the array

print(array)