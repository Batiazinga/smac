import random

# simple implements the simple pi approximation
def simple(n_iter):
    n_hits = 0
    for i in range(n_iter):
        # generate a random position (x,y) in the square
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        # does it fall in the circle?
        if x**2 + y**2 < 1:
            n_hits += 1

    # return the approximation of pi
    return 4.0 * n_hits / float(n_iter)

# start script
n_runs = 10
n_trials = 10000
for i in range(n_runs):
    print simple(n_trials)
