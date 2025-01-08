
import sys
from collections import defaultdict

init_secrets = [int(line) for line in sys.stdin]


def make_secret(secret_number):
    
    secret_number = (secret_number*64)^secret_number
    secret_number  = secret_number%16777216
    secret_number = (secret_number//32)^secret_number
    secret_number  = secret_number%16777216
    secret_number = (secret_number*2048)^secret_number
    secret_number  = secret_number%16777216
        
    return secret_number



total = defaultdict(int)

for num in init_secrets:
    seen = set()
    diffs = []

    for i in range(2000):
        next_num = make_secret(num)
        diffs.append((next_num%10)-num%10)
        num = next_num
        if i>=3:
            if(sequence := tuple(diffs)) not in seen:
                total[sequence]+= num%10
                seen.add(sequence)
            diffs.pop(0)
    
    print(max(total.values()))








    

