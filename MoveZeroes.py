def move_Zeroes(nums):
    quant = nums.count(0)
    m,op = 0,0
    while op < quant:
        if nums[m] == 0:
            del nums[m]
            nums.append(0)
            op += 1
        else:
            m+=1
        
    return nums

print(move_Zeroes([1]))