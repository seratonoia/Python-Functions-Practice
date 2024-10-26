def maxNum(vals):
    maxval = numlist[0]
    for num in numlist:
        if num > maxval:
            maxval = num
    return maxval

def minNum(vals):
    minval = numlist[0]
    for num in numlist:
        if num < minval:
            minval = num
    return minval


import random

numlist = [] #holds 10 randomly generated numbers

for i in range (10):
    numbers = random.randint(0,100)
    numlist.append(numbers)
print(numlist)
print(maxNum(numbers)) #printing function call
print(minNum(numbers))