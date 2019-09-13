# Problem 3
import numpy as np
def check_prob(mean, std, size):
    tot_count = 0
    # get probability 10 times
    for i in range(10):
        # get random number from normal distribution
        x = np.random.normal(mean, std, size)
        # list to store values of the function
        y = []
        for each in x:
            # values of the function at each x
            y.append(each**3+2*each+1)
        count = 0
        # count the number of values bigger than 1
        for each in y:
            if each > 1:
                count += 1
        tot_count += count/size
    return(tot_count/10)
print(check_prob(2, 0.8, 100000))

# Problem 7
# store the number of times that all other students are younger, older than me
count1 = 0
count2 = 0
# store the number of times that at least half are young/older than me
count3 = 0
for i in range(1000000):
    x = random.uniform(0, 1, 18)
    # if I'm the youngest
    if min(x) == x[0]:
        count1 += 1
    # if I'm the oldest
    if max(x) == x[0]:
        count2 += 1
    # if at least half are younger/older than me
    if sorted(x).index(x[0]) >= len(x) // 2:
        count3 += 1
print(count1 / 1000000, count2 / 1000000, count3 / 1000000)
