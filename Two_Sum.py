def twosun(nums, target):
    i = 0
    for i in range(len(nums)):
        for j in range(len(i,len(nums))):
            if nums[i]+ nums[j] == target:
                return [i,j]


n = int(input("quantidade de nums: "))

nums = []

for _ in range(n):
    nums.append(int(input("qual numero: ")))

soma = int(input("soma a ser achada: "))

indice = twosun(nums, soma)

print(f"o nuero {soma} está na soma do {indice}")