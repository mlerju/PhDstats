""" If our data does not follow a normal distribution, we can apply Mann-Whitney U and Kruskal-Wallis H tests.

The Mann-Whitney U test is a nonparametric statistical significance test for determining
whether two independent samples were drawn from a population with the same distribution.

More specifically, the test determines whether it is equally likely that any randomly selected
observation from one sample will be greater or less than a sample in the other distribution.
If violated, it suggests differing distributions.

- Fail to Reject H0: Sample distributions are equal.
- Reject H0: Sample distributions are not equal.
"""

'''
from scipy.stats import mannwhitneyu
data1 = [96.5, 103.5, 76.8, 123.2]
data2 = [5.6, 3.0, 6.3, 6.7]
stat, p = mannwhitneyu(data1, data2)
print("The result of the Mann-Whitney U test is: " + 'Statistics=%.2f , p-value=%.10f  ' % (stat, p))
'''
# First, store data into some variables.
data1 = [77.8, 124.6, 97.7]
data2 = [2.5, 0.6, 1.0]
data3 = [111.3, 94.2, 141.7]
data4 = [1.2, 2.9, 1.7]
data5 = [2.7, 5.0, 2.1]
data = [data1, data2, data3, data4, data5]

"""The Kruskal-Wallis test is a nonparametric version of the one-way analysis of variance test 
or ANOVA for short. It is named for the developers of the method, William Kruskal and Wilson Wallis. 
This test can be used to determine whether more than two independent samples have a different distribution.
It can be thought of as the generalization of the Mann-Whitney U test.

When the Kruskal-Wallis H-test leads to significant results, then at least one of the samples is different
from the other samples. However, the test does not identify where the difference(s) occur. Moreover, 
it does not identify how many differences occur. To identify the particular differences between sample pairs, 
a researcher might use sample contrasts, or post hoc tests, to analyze the specific sample pairs for significant
difference(s). Dunn's test is a non-parametric pairwise multiple comparisons procedure based on rank sums, 
often used as a *post hoc* procedure following rejection of a Kruskal–Wallis test. As such, it is a non-parametric 
analog to multiple pairwise *t* tests following rejection of an ANOVA null hypothesis.

- Fail to Reject H0: All sample distributions are equal.
- Reject H0: One or more sample distributions are not equal.
"""

from scipy.stats import kruskal
stats, p = kruskal(data1, data2, data3, data4, data5)
print("The result of the Kruskal-Wallis H test is: " + 'Statistics = %.2f, p-value = %.10f' % (stats, p))

#These lines of code make PyCharm to show more columns as the output.
import scikit_posthocs as sp
import pandas as pd
pd.set_option('display.max_columns', None)

p_values = sp.posthoc_dunn(data)
print(p_values)