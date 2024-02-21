# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# #Generate Synthetic data
# np.random.seed(42)
# X=2*np.random.rand(100,1) #Random Feature
# y=4+3*X+np.random.randn(100,1) #randn means generate data with noise (Linear Relationship with noise)

# # Creating a Linear Regression Model
# model=LinearRegression()

# # Fit the model to data
# model.fit(X,y)

# #Get the parameters (Slope and Intercept)
# slope=model.coef_[0][0] # Coefficient of line equation made using first data
# intercept=model.intercept_[0] #intercept of first data

# # Make predictions using the model

# X_new=np.array([[0],[2]]) # two new data points for prediction
# y_pred=model.predict(X_new)

# #Plot the data and linear regression line
# plt.scatter(X,y,label='Data points')
# plt.plot(X_new,y_pred,'r-',label=f'Linear Regression Line(y={intercept:.2f}+{slope:.2f}x)')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend
# plt.title('Simple Linear Regrssion Example')
# plt.show()

# Linear Regression
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate synthetic data
np.random.seed(42)
X = 2*np.random.rand(100,1) # Random feature
y =4+3*X+np.random.randn(100,1) #Linear relationship eith noise

# Create a linear regression model
model=LinearRegression()

# Fit the model of data
model.fit(X,y)

#Get the Parameters (slope and intercept)
slope=model.coef_[0][0]
intercept=model.intercept_[0]

# Make predictions using the model
X_new=np.array([[0],[2]]) # two new datapoints for prediction
y_pred=model.predict(X_new)

#Plot the data and the linear regression line
plt.scatter(X,y,label='Data points')
plt.plot(X_new,y_pred,'r-',label=f'Linear Regression Line(y={intercept:.2f}+{slope:.2f}x)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Simple Linear Regression Model')
plt.show()