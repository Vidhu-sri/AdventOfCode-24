from functools import cache


@cache
def func(stones:tuple[int,...], blinks_left:int) -> int:

    if not blinks_left:
        return len(stones)
    
    return sum(func(tuple(apply_rule(stone)), blinks_left-1) for stone in stones)


def apply_rule(stone:int)->list[int]:

    if not stone:
        return [1]
    
    s = str(stone)
    if not len(s)%2:
        mid = len(s)//2
        lhs, rhs = s[:mid], s[mid:]
        return [int(lhs), int(rhs)]

    return [int(s)*2024]

def main():

    with open('input.txt','r') as file:
        stones = file.read().split(' ')
    
    stones = tuple(map(int,stones))

    print(func(stones,blinks_left = 75))


main()

