import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns


ds = pd.read_csv('dataset.csv')

features = ['Hours','Day', 'Month', 'Office_Temperature', 'External_Temperature']
X = ds[features]
y = ds['Energy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#%% LINEAR REGRESSION
m = LinearRegression()
reg = m.fit(X_train, y_train)
pred = reg.predict(X_test)
print(r2_score(y_test, pred))
print('mse', mean_squared_error(y_test, pred))
fig = plt.figure(figsize=(10,10))
plt.scatter(y_test, pred, alpha=0.5)
plt.plot(np.linspace(start = 0, stop = max(y_test)), np.linspace(start = 0, stop = max(y_test)), c = 'red', linewidth = 5)
fig, ax = plt.subplots(figsize = (10,10))
sns.kdeplot(ax = ax, data = y_test, shade=True, legend=False)
sns.kdeplot(ax = ax, data = pred, shade=True, legend=False)
fig, ax = plt.subplots(figsize = (10,10))
errors = pred - y_test
sns.kdeplot(data = errors, shade=True, legend=False, color='r')
#%% POLYNOMIAL REGRESSION
import operator

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

polynomial_features= PolynomialFeatures(degree=9)
x_train = polynomial_features.fit_transform(X_train)
x_test = polynomial_features.fit_transform(X_test)

model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)
rmse = mean_squared_error(y_test,pred)
r2 = r2_score(y_test,pred)
print(rmse)
print(r2, '\n')
fig = plt.figure(figsize=(10,10))
plt.scatter(y_test, pred, alpha=0.5)
plt.plot(np.linspace(start = 0, stop = max(y_test)), np.linspace(start = 0, stop = max(y_test)), c = 'red', linewidth = 5)
fig, ax = plt.subplots(figsize = (10,10))
sns.kdeplot(ax = ax, data = y_test, shade=True, legend=False)
sns.kdeplot(ax = ax, data = pred, shade=True, legend=False)
fig, ax = plt.subplots(figsize = (10,10))
errors = pred - y_test
sns.kdeplot(data = errors, shade=True, legend=False, color='r')
#%%RANDOM FOREST
model = RandomForestRegressor(n_jobs=-1, max_features=3, min_samples_split=3, bootstrap=True,\
                              min_samples_leaf=1, max_depth=300, n_estimators=150)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print('r2', r2_score(y_test, pred))
print('mse', mean_squared_error(y_test, pred))
fig = plt.figure(figsize=(10,10))
plt.scatter(y_test, pred, alpha=0.5)
plt.plot(np.linspace(start = 0, stop = max(y_test)), np.linspace(start = 0, stop = max(y_test)), c = 'red', linewidth = 5)
fig, ax = plt.subplots(figsize = (10,10))
sns.kdeplot(ax = ax, data = y_test, shade=True, legend=False)
sns.kdeplot(ax = ax, data = pred, shade=True, legend=False)
fig, ax = plt.subplots(figsize = (10,10))
errors = pred - y_test
sns.kdeplot(data = errors, shade=True, legend=False, color='r')
