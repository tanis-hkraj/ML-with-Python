import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
x=[2,4,6,3,5,4,7,8,6,1]
y=[6,7,3,4,5,2,8,9,9,4]
c=[1,2,3,4,5,6,7,8,9,10]
fig, ax=plt.subplots()
ax.scatter(x,y,c=c)
ax.set_title("Title")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.show()
