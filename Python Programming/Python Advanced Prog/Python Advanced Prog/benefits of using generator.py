def square_number(nums):
    lst = []
    for num in nums:
        yield num * num


sqr = square_number([1, 2, 3, 4, 5])
for number in sqr:
    print(number)

# better way:
nums = (x*x for x in [1, 2, 3, 4, 5])
print(nums)
for number in nums:
    print(number)
