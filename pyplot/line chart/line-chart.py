import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks = [12, 10, 10, 15, 17, 25, 12, 22, 35, 40]

# plot --> line chart

plt.plot(weeks, marks)

# grid system
plt.grid()

# xlabel & ylabel --> naam milta h x aur y axis ko
plt.xlabel('Weeks')
plt.ylabel('Unit Test Marks')

# show ---> image ready hoti
plt.show()