

def expand(dmap:str)->list:
    res = []

    for i in range(len(dmap)):
        if not i%2:
            res+= int(dmap[i])*[i//2]
        else:
            res+= int(dmap[i])*['.']
    return res

#part1
def move_files(blocks:list):
   
    i,j = blocks.index('.'),len(blocks)-1

    while j>i:
        blocks[i],blocks[j] = blocks[j], blocks[i]

        j-=1
        while blocks[j] == '.':
            j-=1
        i+=1
        while blocks[i] != '.':
            i+=1
    return blocks

def blank_scope(i, blocks):
    return next((j for j in range(i, len(blocks)) if blocks[j] != '.'), len(blocks))


#part2
def move_whole_file(dmap:str,blocks:list):

    dmap = list(map(int,dmap))
    start_pos = [] #prefix sum to get the starting position
    to_append = 0
    for i in range(len(dmap)):
        start_pos.append(to_append)
        to_append+= dmap[i]
  
    #print(len(dmap), start_pos)
    files = [[start_pos[i],dmap[i]] for i in range(len(dmap)-1,-1,-2)]
    

    gaps = [[start_pos[i],dmap[i]] for i in range(1,len(dmap),2)]

    #print(files,gaps, sep='\n')

    for i in range(len(files)):
        file = files[i]
        for j in range(len(gaps)):
            gap = gaps[j]
            #print( blocks)
            if file[1] <= gap[1] and file[0] > gap[0]:
                #print(f'file at index {file[1]},with id {blocks[file[1]]} exchanged with index {gap[1]}')
                file_block = blocks[file[0]:file[0]+file[1]]
                gap_block =  blocks[gap[0]:gap[0]+file[1]]
                blocks[file[0]:file[0]+file[1]],blocks[gap[0]:gap[0]+file[1]] = gap_block,file_block
                gap[0] += file[1]
                gap[1] -= file[1]
        

                break

         
        
#part2           
def check_sum_discontinuous(filesys):
    res = 0
    for idx,file in enumerate(filesys):
        if file != '.':
            res+= file*idx
    return res
            

#part1
def checksum(filesys):

    i = 0
    res = 0
    while filesys[i] != '.' :
        res += i*filesys[i]
        i+=1
    return res

def main():
  
    dmap = input()
  
    exp = expand(dmap)
   
    move_whole_file(dmap,exp)
    
    cs = check_sum_discontinuous(exp)
    print(cs)

main()
    


