import sys
from collections import defaultdict

grid = [list(line.rstrip('\n')) for line in sys.stdin]
visited = set()

in_grid = lambda x,y : 0<=x<len(grid) and 0<=y<len(grid[0])

def find_regions(i, j, side_count):
    
    visited.add((i, j))
    area = 1
    surround = 0

    
    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for x, y in neighbors:
        
        if in_grid(x, y):
            if grid[x][y] == grid[i][j]:
                surround+=1
            if (x, y) not in visited and grid[x][y] == grid[i][j]:
                
                area += find_regions(x, y, side_count)
      
  
    
 
    side_count[surround] += 1
    return area
   


res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if (i,j) not in visited:
          
            
            side_count = defaultdict(int)
            a = find_regions(i,j,side_count)
            print(side_count)
            perimeter = sum([(4-side)*side_count[side] for side in side_count])
            print(a,perimeter)
            res+= a*perimeter
print(res)




    

