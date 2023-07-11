# A mixed array of lists, strings and integers,
# iterate through array and return each item as an integer,
# finally returning the sum of the entire array. 

# Map function returns the specified iterator 
# with the specified function applied to each item
def sum_mix(arr):
    return sum(map(int, arr))


def sum_mix(arr):
    return sum(int(n) for n in arr)