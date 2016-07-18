import random, math

n_iter = 10000
n_hits = 0
var = 0.0

for i in range(n_iter):
    # generate a random position (x,y) in the square
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    obs = 0.0
    # does this random position fall in the circle?
    if x**2 + y**2 < 1.0:
        n_hits += 1
        obs = 4.0
    var += (obs-math.pi)**2

print 4.0 * n_hits / float(n_iter), math.sqrt(var/n_iter)
