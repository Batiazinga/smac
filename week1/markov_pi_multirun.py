import random

def markov_pi(n_iter, delta):
    # starting point
    x, y = 1.0, 1.0
    # number of hits in the circle
    n_hits = 0

    for i in range(n_iter):
        # pick a random next position
        dx, dy = random.uniform(-delta, delta), random.uniform(-delta, delta)
        new_x, new_y = x+dx, y+dy

        # is new position in the square?
        if abs(new_x) < 1.0 and abs(new_y) < 1.0:
            # yes, in the square -> update position
            x, y = new_x, new_y
        # else, stay at the same position (i.e. tile)

        # is position in the circle?
        if x**2 + y**2 < 1.0:
            n_hits += 1

    # compute pi
    return 4.0 * n_hits / float(n_iter)

# start script
n_runs = 10
n_trials = 10000
delta = 0.1
for i in range(n_runs):
    print markov_pi(n_trials, delta)
