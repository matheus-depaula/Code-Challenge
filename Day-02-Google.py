""" This problem was recently asked by Google.
Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.
Bonus: Can you do this in one pass? """

def verify_num(nList, k):
    for num_1 in nList:
        for num_2 in nList:
            if num_1 + num_2 == k:
                return True
    return False

print(verify_num([10, 15, 3, 7], 17))
