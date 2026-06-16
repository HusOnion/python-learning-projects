
# defining the search method
def interpolation_search(array, target):
    countOfProbes = 0  # to count how much round will it take to find the target

    # setting the high and the low indecies values 
    high = len(array) - 1 
    low = 0

    
    while low <= high and target >= array[low] and target <= array[high]:

        # the formula needed
        probe = int(low + (high - low) * (target - array[low]) / (array[high] - array[low]))

        countOfProbes += 1

        
        if probe < low or probe > high:
            return -1,countOfProbes # a sentinal value 

        if array[probe] == target:
            return probe,countOfProbes

        # sets the new low or the new high
        elif array[probe] < target:
            low = probe + 1
        else:
            high = probe - 1
 
    return -1,countOfProbes


numbers =  [2,5,9,12,25,56,100,101,180]

index,count = interpolation_search(numbers,56)
print(f"Found at index: {index}")
print(f"COUNT: {count}")
