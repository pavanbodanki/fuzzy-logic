# Importing pandas to open the dataset
import pandas as pd
# This function returns the Pearson correlation coefficient value of each row with respect to
output row
def pearsonr(x, y):
n = len(x)
sum_x = float(sum(x))
sum_y = float(sum(y))
sum_x_sq = sum(map(lambda x: pow(x, 2), x))
sum_y_sq = sum(map(lambda x: pow(x, 2), y))
psum = sum(map(lambda x, y: x * y, x, y))
num = psum - (sum_x * sum_y/n)
den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
if den == 0: return 0
return num / den
# Reading the dataset
res = pd.read_excel("Book1.xlsx")
# storing the values of each row
x = res['Projects'].values
x1 = res['Coding Skills '].values
x2 = res['Aptitude Skills'].values
x3 = res['Technical Skills '].values
x4 = res['Communication Skills'].values
x5 = res['Academic Performance'].values
x6 = res['Programming Skills'].values
x7 = res['Management Skills'].values
x8 = res['Internships'].values
x9 = res['Backlog'].values y = res[' Placed'].values
# Calling pearson function for each value
d =
[pearsonr(x,y),pearsonr(x1,y),pearsonr(x2,y),pearsonr(x3,y),pearsonr(x4,y),pearsonr(x5,y),pearsonr(x6, y),pearsonr(x7,y),pearsonr(x8,y),pearsonr(x9,y)]
# Prints the rows whose correlation coefficient is greater than 0.6
for i in d:
  if i >= 0.7:
  print(i)
