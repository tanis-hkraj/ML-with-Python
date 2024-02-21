import seaborn as sns
import matplotlib.pyplot as plt
#load the iris dataset
iris=sns.load_dataset("iris")

#Create a pairplot
sns.pairplot(iris,hue="species")
plt.show()