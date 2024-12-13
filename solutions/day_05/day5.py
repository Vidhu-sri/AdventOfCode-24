

from collections import defaultdict

with open("input.txt", "r") as file:
    input_lines = file.read().strip().split("\n")

before = defaultdict(set)
after = defaultdict(set)
res = 0
corrections = 0

#part1
def func(nums):

    for i in range(len(nums)):
        for j in range(len(nums)):

            if ((j>i and nums[j] not in after[nums[i]]) or 
                j<i and nums[j] not in before[nums[i]]):
                    return False
    return nums[(len(nums)//2)]
            

#part2        
def correct(nums):
    
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] in after[nums[j+1]]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)//2]


for line in input_lines:

    if not line:
        continue
    if '|' in line:
        num1,num2 = map(int,line.split('|'))
        before[num2].add(num1)
        after[num1].add(num2)
    else:
        nums = list(map(int,line.split(',')))
        to_add = func(nums)
        if to_add:
            res+= to_add
        else:
            corrections+=correct(nums)
print(res)
print(corrections)





        