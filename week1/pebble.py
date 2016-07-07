import random

# sites
#
# 0 1 2
# 3 4 5
# 6 7 8

# inputs
n_iter = 1000000
weights = [3.0, 1.0, 3.0, 1.0, 0.5, 1.0, 3.0, 1.0, 3.0]
neighbours = [[0, 0, 1, 3], [0, 1, 2, 4], [1, 2, 2, 5],
        [0, 3, 4, 6], [3, 1, 5, 7], [4, 5, 2, 8],
        [6, 6, 3, 7], [6, 4, 7, 8], [7, 8, 8, 5]]

# result
histo = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# algo
pos = 0
for i in range(n_iter):
    # random next position
    next = neighbours[pos][random.randint(0, 3)]
    # is the move rejected?
    if random.uniform(0.0, 1.0) < weights[next] / weights[pos]:
        pos = next

    # register position
    histo[pos] += 1

# Compare true weight and estimated weight
norm = sum(weights)
for i in range(9):
    print 'site {}: weight {}, result {}'.format(i, weights[i], norm * histo[i] / float(n_iter))
