import seaborn as sns
import matplotlib.pyplot as plt
#load the iris dataset
iris=sns.load_dataset("iris")

# Choose a feature for CDF (e.g. sepal_length)
feature1="sepal_length"
feature2="petal_length"
data1=iris[feature1]
data2=iris[feature2]

# Create CDF using seaborn's ecdfplot
sns.ecdfplot(data1,stat="proportion",complementary=True)
sns.ecdfplot(data2,stat="proportion",complementary=True)

# Add labels and title
plt.xlabel(f'{feature1}')
plt.ylabel('Cumulative Probability')
plt.title(f'Cumulative Distribution Function (CDF): {feature1}')


#show the plot


plt.xlabel(f'{feature2}')
plt.ylabel('Cumulative Probability')
plt.title(f'Cumulative Distribution Function (CDF): {feature2}')
plt.show()