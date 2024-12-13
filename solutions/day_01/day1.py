import heapq
import sys
from collections import defaultdict



heap1 = []
heap2 = []


for line in sys.stdin:
    nums = tuple(map(int,line.split()))
    heapq.heappush(heap1,nums[0])
    heapq.heappush(heap2,nums[1])
  

counter = defaultdict(int)

#part1
res = 0
nums = []
while heap1 and heap2:
    a = heapq.heappop(heap1)
    b = heapq.heappop(heap2)
    nums.append(a)
    counter[b]+=1


    res+= abs(a-b)
print(res)

#part2
print('similiarity:','\n')
res = 0
for num in nums:
    res+= num*counter[num]
print(res)
