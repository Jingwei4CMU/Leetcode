import pandas as pd
import operator

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

x = pd.read_excel('/Volumes/More/Courses/12761/HW2/temp.xlsx', sheet_name='Sheet1')
y = pd.read_excel('/Volumes/More/Courses/12761/HW2/cons.xlsx', sheet_name='Sheet1')
x = np.array(x)
y = np.array(y)
X = x
reg = LinearRegression().fit(X, y)
reg.score(X, y)
print(reg.coef_)
print(reg.intercept_)
print(reg.score(X, y))
plt.plot(X, y, 'b.')
pre = reg.predict(X)
plt.plot(X, pre, 'r-')
plt.xlabel('temperature')
plt.ylabel('energy consumption')
plt.show()
error = np.sqrt(mean_squared_error(y,reg.predict(X)))
print("error1:", error)


polynomial_features= PolynomialFeatures(degree=3)
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
r2 = r2_score(y, y_poly_pred)
print(rmse)
print(r2)

print(model.coef_)

plt.scatter(x, y, s=10)
# sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(X, y, 'b.')
plt.plot(x, y_poly_pred, color='r')
plt.xlabel('temperature')
plt.ylabel('energy consumption')
plt.show()
print('error2 %.2f',rmse)
