
#part1 brute force

from collections import deque
from tqdm import tqdm

def num_stones(stones, blinks):
    
    
    for _ in tqdm(range(blinks), desc = "performing blink", unit='line', ncols = 80):
        
        changes = deque()
   
        sync = 0
        for i in range(len(stones)):

          
            
            if stones[i] == '0':
                stones[i] = '1'

            elif not len(stones[i])%2:
                left_half = str(int(stones[i][:len(stones[i])//2]))
                right_half = str(int(stones[i][len(stones[i])//2:]))
                
                changes.append((left_half,right_half, i+sync))
                sync+=1
        

            else:
                stones[i] = str(int(stones[i])*2024)
            
        
        while changes:
            change = changes.popleft()
            left_val = change[0]
            right_val = change[1]
            idx = change[2]

            stones[idx] = left_val
            stones.insert(idx+1, right_val)
          

        
    return len(stones)


def main():
    initial = input().split(' ')
    res = num_stones(initial,blinks=25) #for part1 blinks = 25
    print(res)

main()
    
