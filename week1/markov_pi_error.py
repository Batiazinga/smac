import random, math, pylab

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

n_runs = 500
for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
    n_trials_list = []
    error_list = []
    for poweroftwo in range(4, 13):
        n_trials = 2 ** poweroftwo
        n_trials_list.append(n_trials)
        error = 0.0
        for i in range(n_runs):
            error += (markov_pi(n_trials, delta) - math.pi)**2
        error_list.append(math.sqrt(error / float(n_runs)))
    pylab.plot(n_trials_list, error_list, 'o', ms = 8, label='$\delta = $' + str(delta))

pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('number of trials')
pylab.ylabel('root mean square deviation')
pylab.plot([10,10000],[1.642 / math.sqrt(10.0), 1.642 / math.sqrt(10000.0)], label = 'direct')
pylab.title('Markov-chain sampling of pi: root mean square deviation vs. n_trials')
pylab.legend(loc='upper right')
pylab.savefig('markov_sampling_rms_deviation.png')
pylab.show()
