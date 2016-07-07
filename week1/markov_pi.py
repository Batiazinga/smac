import random

# starting point
x, y = 1.0, 1.0
# maximum amplitude of the small moves
delta = 0.1
# number of iteration
n_iter = 4000
# number of hits in the circle
n_hits = 0

for i in range(n_iter):
    # pick a random next position
    dx, dy = random.uniform(-delta, delta), random.uniform(-delta, delta)

    # is new position in the square?
    if abs(x+dx) < 1.0 and abs(y+dy) < 1.0:
        # yes, in the square -> update position
        x, y = x+dx, y+dy
    # else, remain at the same position

    # is position in the circle?
    if x**2 + y**2 < 1.0:
        n_hits += 1

# compute pi
pi = 4.0 * n_hits / float(n_iter)

# print result
print 'The value of PI is approximately {}'.format(pi)
