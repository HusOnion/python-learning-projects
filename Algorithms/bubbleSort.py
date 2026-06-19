# its not the best sorting algorithm but its kinda basic and easy to understand

array = [5, 2, 9, 1, 5, 6]

def bubble_sort(array):
    for i in range(len(array)): # iterate over the array
        for j in range(0, len(array)-i-1): # iterate over the unsorted part of the array
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j] # swap if the element found is greater than the next element


bubble_sort(array)
print(array)