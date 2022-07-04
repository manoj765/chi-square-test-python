# importing packages
import scipy.stats as stats
import numpy as np

# no of hours a student studies
# in a week vs expected no of hours
observed_data = [15, 27, 34, 24,] 
expected_data = [25, 25, 25, 25,]


# Chi-Square Goodness of Fit Test
chi_square_test_statistic, p_value = stats.chisquare(
	observed_data, expected_data)

# chi square test statistic and p value
print('chi_square_test_statistic is : ' +
	str(chi_square_test_statistic))
print('p_value : ' + str(p_value))


# find Chi-Square critical value
print("cv is:")

print(stats.chi2.ppf(1-0.05, df=3))

# CONCLUSION

x=int(chi_square_test_statistic)

c=(stats.chi2.ppf(1-0.05, df=3))

if (x <= c):

 print("The conclusion is:")    
 print("Accept null hypothesis.")
else:
 print("Reject null hypothesis.")









