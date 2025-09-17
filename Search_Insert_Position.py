def searchInsert(nums, target):
    baixo = 0
    alto = len(nums) - 1
    nums.sort()
    while baixo <= alto:
        meio = int((baixo + alto)/2)
        escolhido = nums[meio]
        if target == escolhido:
            return meio
        elif escolhido > target:
            alto = meio-1
        elif escolhido < target:
            baixo = meio+1
    return baixo

print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3], 4))