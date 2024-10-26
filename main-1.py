def maxNum(vals):
    maxval = numlist[0]
    for num in range(len(numlist)):
        for i in range (numbers):
            if numlist[i] > maxval:
                maxval = numlist[i]
    return maxval
    


import random
numlist = []
for i in range (10):
    numbers = (random.randint(0,100))
    numlist.append(numbers)
print(numbers)
print(maxNum(numbers))