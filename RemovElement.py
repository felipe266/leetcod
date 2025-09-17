def removeElement(num, val):
    tam = len(num)
    i = 0
    while i < tam:
        if num[i] == val:
            num.remove(val)
            tam -= 1
        else:
            i += 1
    return i

num = [0,1,2,2,3,0,4,2]
val = 2

k = removeElement(num, val)

print(k, num)