import numpy as np
import scipy.stats as st

import matplotlib.pyplot as plt
import SLACplots

# Example 1, a simple plot with some line series
# and some error bar points

fig = plt.figure()

# lines
x = np.linspace(0, 5, 1000)

# some random functions
n_series = 6
w = np.arange(n_series)[:,None]
b = 0.1*np.arange(n_series)[:,None]
y = w*np.sin(x)**2 + x + b

plt.plot(x, y.T)

# errorbar points
n_samples = 6
x_samples = np.arange(n_samples)

# a random function
y_mean = 10 - 3*x_samples
y_error_upper = 2*np.ones_like(x_samples)
y_error_lower = np.abs(3*np.sin(10*x_samples))
# unfortunately, some args are not enabled by default
# for errorbars, specify `fmt = 'o'`
plt.errorbar(x_samples,
             y_mean,
             yerr = (y_error_lower,
                     y_error_upper),
             fmt = 'o')

# a random function
plt.xlabel(r'Time [$\mu$s]')
plt.ylabel(r'$\int f(x) e^{i \lambda x} \; dx$')

plt.tight_layout()

# Example 2: a histogram with model fit
# and an error band plot with legend

fig = plt.figure()

# histogram with some binned data
mean = 2
std = 0.5
n_samples = 1000

bin_edges = np.linspace(-4, 4, 26)
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

plt.hist(np.random.normal(mean, std, n_samples),
         bins = bin_edges,
         histtype = 'step',
         linewidth = 3,
         label = 'Observation')

# and an expectation value with error
cdf = st.norm.cdf(bin_edges,
                  loc = mean,
                  scale = std)
idf = n_samples*np.diff(cdf)
plt.errorbar(bin_centers,
             idf,
             yerr = np.sqrt(idf),
             fmt = 'o',
             label = 'Model Prediction'
             )

# add an error band for no good reason
x = np.linspace(-4, 4, 1000)

# just an interesting shape in a place that's not disruptive
y = - 4*x + 100
yerr = 10*np.sin(x) + 8 + 2*x**2

# I usually plot these with the band having alpha = 0.5
# and the middle line with alpha = 1
plt.fill_between(x,
                 y-yerr,
                 y+yerr,
                 color = SLACplots.stanford.poppy,
                 alpha = 0.5)
plt.plot(x,
         y,
         color = SLACplots.stanford.poppy,
         label = 'Some Other Thing')

plt.legend()
plt.xlabel(r'Measured Energy [MeV]')
plt.ylabel(r'$\Phi$ [MeV$^{-1}$s$^{-1}$]')
plt.tight_layout()
plt.show()
