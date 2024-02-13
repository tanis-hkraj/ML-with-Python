import numpy as np
class Perceptron(object):
    def __init__(self,eta=0.01,n_iter=50,random_state=1):
        self.eta=eta # Learning rate by default=0.01
        self.n_iter=n_iter # Epochs=50
        self.random_state=random_state # Supports shuffling of training data
    def fit(self,X,Y): # Gradient Descent to decrease the Error
        rgen=np.random.RandomState(self.random_state)
        self.w_=rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_=[] # stepwise determine the error value by gradient
        for _ in range(self.n_iter):
            errors=0
        for xi, target in zip(X,Y): # adjusting weights to reduce error
            update=self.eta * (target - self.predict(xi))
            self.w_[1:]+=update*xi
            self.w_[0]=update
            error+=int(update!=0.0)
            self.errors_.append(errors)
        return self
    def net_input(self,X):
        return np.dot(X,self.w_[1:])+self.w_[0]
    def predict(self,X):
        return np.where(self.net_input(X)>=0.0,1,-1)

from sklearn import datasets
iris=datasets.load_iris()
X=iris.data[:,[2,3]] #Every row in 2nd and 3rd column
y=iris.target
print('Class labels:',np.unique(y))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.7,random_state=1,stratify=y)
print('Labels counts in y:',np.bincount(y))
print('Labels count in y_train:',np.bincount(y_train))
print('Labels count in y_test:',np.bincount(y_test))


from sklearn.preprocessing import StandardScaler
sc=StandardScaler() #Normalisation means to make data in between 0 and 1
sc.fit(X) # Training data fed for standardization
X_train_std=sc.transform(X_train) # transforming the data to standardized data
X_test_std=sc.transform(X_test) # transforming the data to standardized data

from sklearn.linear_model import Perceptron
ppn=Perceptron(eta0=0.1,random_state=1)
ppn.fit(X_train_std,y_train)
y_pred=ppn.predict(X_test_std)
print('Missclassified examples: %d'%(y_test!=y_pred).sum())

            