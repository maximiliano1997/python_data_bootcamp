# Given an empty list "random_values", write a Python function
# called "random_value_consumer" which takes 2 parameters
# of any data type in and adds the both parameters to that list.

random_values = []
input_user_list = []


def random_value_consumer(one, two):
    input_user_list.append(one)
    input_user_list.append(two)
    random_values.extend(input_user_list)
    return random_values


print(random_value_consumer('lol', 3))

# Write a new function called "analyse_list_elements" which takes 1 parameter.
# The function should print the length of
# each element of that list with its value and type.


def analyse_list_elements(arg):
    for i in arg:
        a = len(str(i))
        b = type(i)
        print(f'{a} {i} -> {b}')


print(analyse_list_elements(random_values))

##########
print("extra\n\n")


def random_value_consumer(a, b):
    random_values.extend(a)
    random_values.extend(str(b))
    return [random_values]


random_value_consumer("imanol", 27)
print(random_values)

##########


def append_values(a, b):
    random_values.append(a)
    random_values.append(b)


def random_value_consumer(a, b) -> list:
    append_values(a, b)
    # random_value.append(b)
    return [random_values]


# return method needs brackets of what is to returned

random_value_consumer("Imanol", 27)
print(random_values)


def analyse_list_elements(random_values):
    for x in random_values:
        a = len(str(x))
        b = type(x)
        print(f'{b} {x} -> {a}')


analyse_list_elements(random_values)
