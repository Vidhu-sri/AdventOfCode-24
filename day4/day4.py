import sys
from itertools import combinations

class TrieNode:

    def __init__(self):
        self.next = {}
        self.isterminal = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def addword(self, word):
        curr = self.root
        for char in word:
            if not curr.next.get(char,None):
                curr.next[char] = TrieNode()
            curr = curr.next[char]
        
        curr.isterminal = True


def word_search(ptr: TrieNode, i:int, j:int, dx:int, dy:int,grid:list[list[str]])->bool:

    if ptr.isterminal:
        return True
    
    
    
    
    x,y = i+dx,j+dy

    if 0<=x<len(grid) and 0<= y < len(grid[0]):

        if ptr.next.get(grid[x][y],None):

            if word_search(ptr.next[grid[x][y]],x,y,dx,dy,grid):
               
                return True
            
    return False



def main():

    grid = [list(line.rstrip('\n')) for line in sys.stdin]
    m,n = len(grid), len(grid[0])
    trie = Trie()
    trie.addword('XMAS')
    neighbors = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1), (-1,-1)]
    
    res = 0
    for i in range(m):
        for j in range(n):

            curr = trie.root
            if curr.next.get(grid[i][j], None) and grid[i][j] == 'X':
                
                curr = curr.next[grid[i][j]]
                for neighbor in neighbors:
                    dx,dy = neighbor
                    
                    if word_search(curr, i,j,dx,dy,grid):
                        print(i,j, f'({dx,dy})')
                        res+=1
                
 
    print(res)




main()

        

