'''y = w0 + w1x + w2x^2 + w3x^3 +....+ wdx^d  
in the aove equation w0 is Bias
d is degree of polynomial'''
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score,mean_squared_error
X=np.array([258.0,270.0,294.0,320.0,342.0,396.0,368.0,446.0,480.0,586.0])[:,np.newaxis]
y=np.array([236.0,234.0,252.0,298.0,314.0,342.0,360.0,391.2,390.8,432.0])[:,np.newaxis]
lr=LinearRegression() #for simple linear regression
pr=LinearRegression() # for polynomial regression

quadratic=PolynomialFeatures(degree=2)
x_quad=quadratic.fit_transform(X)
# Training the LinearRegression Model for comparison
lr.fit(X,y)
X_fit=np.arange(250,600,10)[:,np.newaxis]
y_lin_fit=lr.predict(X_fit)
pr.fit(x_quad,y)
y_quad_fit=pr.predict(quadratic.fit_transform(X_fit))

# Ploting the result
plt.scatter(X,y,label='Training Data Points')
plt.plot(X_fit,y_lin_fit,label='Linear Fit',linestyle='--')
plt.plot(X_fit,y_quad_fit,label='Quadratic Fit')
plt.legend(loc='upper left')
plt.show()

y_lin_pred=lr.predict(X)
y_quad_pred=pr.predict(x_quad)

print("MSE of LINEAR: %.3f, MSE of QUADRATIC: %.3f"%(mean_squared_error(y,y_lin_pred),mean_squared_error(y,y_quad_pred)))
print("R2_Score of LINEAR: %.3f, R2_Score of QUADRATIC: %.3f"%(r2_score(y,y_lin_pred),r2_score(y,y_quad_pred)))



