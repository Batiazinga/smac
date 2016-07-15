import random, math, pylab

# direct_pi implements the simple pi approximation
def direct_pi(n_iter):
    n_hits = 0
    for i in range(n_iter):
        # generate a random position (x,y) in the square
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        # does it fall in the circle?
        if x**2 + y**2 < 1:
            n_hits += 1

    # return the approximation of pi
    return 4.0 * n_hits / float(n_iter)

# number of runs
n_runs = 100
# store number of trials for each estimation
n_trials_list = []
# compute and store the rms for each estimation
rms_list = []

# start algo
for poweroftwo in range(4, 13):
    # number of trials
    n_trials = 2 ** poweroftwo
    n_trials_list.append(n_trials)
    # compute rms for this number of trials
    rms = 0.0
    for run in range(n_runs):
        rms += (direct_pi(n_trials) - math.pi) ** 2
    rms_list.append(math.sqrt(rms / n_runs))

# plot results
pylab.plot(n_trials_list, rms_list, 'o')
pylab.plot([10.0, 10000.1], [1.642/math.sqrt(10.0), 1.642/math.sqrt(10000.0)])
pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('number of trials')
pylab.ylabel('root mean square deviation')
pylab.title('Direct sampling of pi: root mean square deviation vs. n_trials')
pylab.savefig('direct_sampling_rms_deviation.png')
pylab.show()
