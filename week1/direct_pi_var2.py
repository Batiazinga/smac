import random, math

n_iter = 10000
m1 = 0.0
m2 = 0.0

for i in range(n_iter):
    # generate a random position (x,y) in the square
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    obs = 0.0
    # does this random position fall in the circle?
    if x**2 + y**2 < 1.0:
        obs = 4.0
    m1 += obs
    m2 += obs ** 2

m1 /= n_iter
m2 /= n_iter
print m1, m2, math.sqrt(m2 - m1**2)
