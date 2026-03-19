from numpy import random
def flip_run_through():
    heads = 0
    flip_count = 0
    while heads <= (flip_count-heads):
        x = random.rand()
        if x <= 0.5:
            flip_count += 1
            heads += 1
        elif x >= 0.5:
            flip_count += 1
    return heads/flip_count
total = 0
sequences_count = 0
while True:
    sequences_count += 1
    total += flip_run_through()
    print(4*total/sequences_count)



    

