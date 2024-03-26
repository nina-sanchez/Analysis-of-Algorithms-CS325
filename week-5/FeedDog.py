# greedy algorithm
# pick greedy option at first then pick second best ....

def feedDog(hunger_level, biscuit_size):
    # first we want to sort the list from highest to lower --> to obtain how we will find greedy way
    # from geeks for geeks I saw how to sort list largest to smallest: https://www.programiz.com/python-programming/methods/list/sort
    hunger_level.sort(reverse = True) # by sorting from highest to lowest, then we are picking greedy
    biscuit_size.sort(reverse = True)
    
    hunger = len(hunger_level) # to use to iterate through in loop
    biscuit = len(biscuit_size) # to use to iterate through in loop
    count = 0 # return total count of feed poochies
    fed_poochies = set() # to not re use biscuits
    
    for i in range(hunger): # iterate through hunger level list
        dogs = hunger_level[i]
        for j in range(biscuit): # iterate through biscuit hunger level
            food = biscuit_size[j]
            if (food >= dogs and food not in fed_poochies): # from hw assignment, if biscuits >= food
                count += 1
                fed_poochies.add(food)
                break
    return count


# example 1
# hunger_level = [1,2,3]
# biscuit_size = [1,1]
# Output: 1

# Example 2:
# hunger_level2 = [2, 1]
# biscuit_size2 = [1,3,2]
# Output: 2

# feedDog(hunger_level, biscuit_size)
# feedDog(hunger_level2, biscuit_size2)


