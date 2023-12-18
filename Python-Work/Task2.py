# 2. Given is a list between numbers from 0 to 100. All numbers which have a 5 as a digit like: 5, 15, 95 should be counted and stored in a new list variable. Please return the total number of entries in that list and the list itself.
# create a list with a range of numbers from 0 to 100
# add all digits with a 5 in it to another variable list and count how many numbers are in there
my_list = []

# for loop to get all the numbers from 0 to 100
for i in range(1, 101):
    if "5" in str(i):
        # since i will be an integer, had to make sure to change it to a string
        my_list.append(i)
    # adding the number to the list if it contains a 5 in it


print(my_list)
print(len(my_list))
