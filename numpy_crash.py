import numpy as nm
from scipy import stats
salary = [0, 1, 2, 3, 4, 6, 8, 9, 9, 10, 10, 11, 14]

temp=[93,84,82,78,98,70]
number_of_people=[13,10, 11, 8, 15, 9]

print('mean : ', nm.mean(salary))
print('median : ', nm.median(salary))
print('mode : ', stats.mode(salary))
print('range : ', nm.max(salary) - nm.min(salary))
print('var : ', nm.var(salary))
print('std : ', nm.std(salary))
print('covariance : ', nm.cov(temp, number_of_people))
print('correlation : ', nm.corrcoef(temp, number_of_people))
