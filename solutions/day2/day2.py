

import sys
import numpy as np
#part1
def is_safe(nums:list)->bool:
    valid_diff_pos = {1,2,3}
    valid_diff_neg = {-1,-2,-3}
    return (all(nums[i]-nums[i-1] in valid_diff_pos for i in range(1,len(nums))) or 
            all(nums[i]-nums[i-1] in valid_diff_neg for i in range(1,len(nums))))

#part2

def dampener(nums:list)->bool:

    if is_safe(nums):
        return True
    

    for i, _ in enumerate(nums):
        copy = nums.copy()
        copy.pop(i)

        np_copy = np.array(copy)
        diff = np.diff(np_copy)
        if np.logical_and(diff>=1,diff<=3).all() or np.logical_and(diff>=-3,diff<=-1).all():
            return True
    return False
 

#res = 0
damp_safe = 0
for line in sys.stdin:

    nums = list(map(int,line.split()))
    #res+= is_safe(nums)
    damp_safe+= dampener(nums)

print(damp_safe)
