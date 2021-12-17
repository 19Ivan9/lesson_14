def fun():
    a = 4
    b = 5
    c = 8
    print(a, b, c)
    return fun.__code__.co_nlocals


def test_fun():
    return print(fun())


test_fun()

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(nums, func1, func2):
    if [num for num in nums if num < 0]:
        return func2(nums)
    return func1(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
