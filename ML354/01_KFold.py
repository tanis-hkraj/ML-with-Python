from sklearn.datasets import load_iris
dataset=load_iris()
x=dataset.data
y=dataset.target 

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3) # 
x_val,x_test,y_val,y_test=train_test_split(x_test,y_test,test_size=0.5)#x and y validation set
# training data = 70% and test data=30%
#for 30% test data (at last testing data=15% & validation data=15%)

from sklearn.decomposition import PCA # dimensionality reduction technique
from sklearn.preprocessing import StandardScaler #normalisation
from sklearn.linear_model import Perceptron # 2-class Classifier
from sklearn.pipeline import Pipeline # for streamlining all the phases in one module together

p=Pipeline([('sc',StandardScaler()),('pca1',PCA(n_components=3)),('p',Perceptron(penalty='l2'))])
# L1 -> Lasso Regularization
# L2 -> Ridge Regularization
# L1+L2 -> Elastic Regularization
p.fit(x_train,y_train)
train_pred1=p.predict(x_train)
val_pred1=p.predict(x_val)

from sklearn.metrics import accuracy_score
print("Training Accuracy: ",accuracy_score(train_pred1,y_train))
print("Validation Accuracy: ",accuracy_score(val_pred1,y_val))


p1=Pipeline([('sc',StandardScaler()),('pca1',PCA(n_components=3)),('p',Perceptron(penalty='l1'))])
# L1 -> Lasso Regularization
# L2 -> Ridge Regularization
# L1+L2 -> Elastic Regularization
p1.fit(x_train,y_train)
train_pred2=p1.predict(x_train)
val_pred2=p1.predict(x_val)

# from sklearn.metrics import accuracy_score
print("Training Accuracy: ",accuracy_score(train_pred2,y_train))
print("Validation Accuracy: ",accuracy_score(val_pred2,y_val))

# Make use of LDA (Components = 2),penalty is L1 and L2

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
p3=Pipeline([('sc',StandardScaler()),('lda',LDA(n_components=2)),('p',Perceptron(penalty='l1'))])
p3.fit(x_train,y_train)

train_pred4=p3.predict(x_train)
val_pred4=p3.predict(x_val)
from sklearn.metrics import accuracy_score
print("Training Accuracy: ",accuracy_score(train_pred4,y_train))
print("Validation Accuracy: ",accuracy_score(val_pred4,y_val))

#First Method of KFold

from sklearn.model_selection import KFold
k=5
kf=KFold(n_splits=k,shuffle=True)
acc_score=[]

for train_index,test_index in kf.split(x):
    X_train=[]
    X_test=[]
    Y_train=[]
    Y_test=[]
    for i in train_index:
        X_train.append(x[i])
        Y_train.append(y[i])
    for i in test_index:
        X_test.append(x[i])
        Y_test.append(y[i])
        
p.fit(X_train,Y_train)
test_pred=p.predict(X_test)
acc_score.append(accuracy_score(test_pred,Y_test))
print(acc_score)
import numpy as np
print("Accuracy: ",np.average(acc_score))
