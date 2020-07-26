""" This problem was asked by Uber.
Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in 
the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division? """

new_list = []

def calculate_new_array(list_1):
    count = 1

    for i in list_1:
        for j in list_1:
            if j != i:
                count *= j
        new_list.append(count)
        count = 1
    return print(new_list)

calculate_new_array([1, 2, 3, 4, 5])
