# Q2. What is the difference between remove() and pop() functions in Python?

# Basically remove() and pop() functions is used for delete any elemant inside the lists. But in both of them a huge difference:


# Remove function
# If we use remove() then it removes elemant but if that elemant is not present in the list that time it is showing error. Ex:
l = [2, 4 ,6 , 8, 10, 12 ,14, 16, 18, 20]
# l.remove(800)
# print(l) 
#Output: ValueError: list.remove(x): x not in list



# If we use pop() then it removes the last elemant in the lsit. If you want to remove any middle elemant in this list then you can write the index number of this elemant inside the parentesis

# pop function's example 
l.pop()    # It removes the last elemant
l.pop(2)  # It removes the 2nd index elemant. 
print(l)