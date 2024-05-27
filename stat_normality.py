'''First, let's see if our data adjust to a normal distribution with two tests: Kolmogorov-Smirnov and Shapiro-Wilk.
In these tests, H0 or null hypothesis states that data fit to normal distribution, H1 or alternative hypothesis infers
data does not fit to normal distribution.'''

from scipy.stats import kstest
from scipy.stats import shapiro

data = [77.8, 124.6, 97.7,
        2.5,0.6,1.0,
        111.3,94.2,141.7,
        1.2,2.9,1.7,
        2.7,5.0,2.1]

test_ks = kstest(data, 'norm')
test_sh = shapiro(data)

print("Kolmogorov-Smirnov test: ", test_ks)
print("Shapiro-Wilk test: ", test_sh)