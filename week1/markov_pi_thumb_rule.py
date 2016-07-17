import random

def markov_pi_acceptance(n_iter, delta):
    """
    markov_pi_acceptance runs the markov pi estimation algorithm
    but does not compute pi.
    Instead it computes the acceptance rate.
    """
    # starting point
    x, y = 1.0, 1.0
    # number of accepted moves
    n_accepted = 0

    for i in range(n_iter):
        # pick a random next position
        dx, dy = random.uniform(-delta, delta), random.uniform(-delta, delta)

        # is new position in the square?
        if abs(x+dx) < 1.0 and abs(y+dy) < 1.0:
            # yes, in the square -> accepted
            n_accepted += 1
            x, y = x+dx, y+dy
        # else, rejected

    # compute acceptance rate
    return n_accepted / float(n_iter)

n_trials = 2 ** 12
print 'delta: acceptance rate'
for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
    print '{}: {}'.format(delta, markov_pi_acceptance(n_trials, delta))
