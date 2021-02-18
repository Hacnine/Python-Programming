# Python3 code to demonstrate yield keyword

# Checking number of occurrence of
# geeks in string

# generator to print even numbers
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i


# initializing string
test_string = " The are many geeks around you, geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0
print("The number of geeks in string is : ", end="")
test_string = test_string.split()

for j in print_even(test_string):
    count = count + 1

print(count)
