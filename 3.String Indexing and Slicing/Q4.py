# Q.4 For the variable: word variable = 'Panaji@12256'
# Calculate the following:
# (a) Total number of alphabets in lowercase
# (b) Total number of alphabets in uppercase
# (c) Total number of numerical in string


word_variable = 'Panaji@12256'

# Count the number of lowercase alphabets
lower_count = sum(1 for char in word_variable if char.islower())

# Count the number of uppercase alphabets
upper_count = sum(1 for char in word_variable if char.isupper())

# Count the number of numerical characters
num_count = sum(1 for char in word_variable if char.isdigit())

# Print the results
print("Total number of lowercase alphabets:", lower_count)
print("Total number of uppercase alphabets:", upper_count)
print("Total number of numerical characters:", num_count)
