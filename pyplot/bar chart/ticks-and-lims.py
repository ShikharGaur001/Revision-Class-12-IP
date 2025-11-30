import matplotlib.pyplot as plt

a=[11,17,15,19]
b=[14,16,18,15]
plt.bar(a,b)
#* ticks
plt.xticks([11,17,15,19],[1,2,3,4])

#* lims
plt.xlim(-2.0,20)
plt.show()