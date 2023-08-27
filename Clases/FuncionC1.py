def duplicados(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,2,4]
print(duplicados(nums))
