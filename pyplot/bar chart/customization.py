import matplotlib.pyplot as plt

x=[0,1,2]
y=[10.2,15.8,5.9]

# plt.bar(x,y,width=0.5)
# plt.show()

#* default width --> 0.8
# plt.bar(x,y,width=[0.5,0.7,0.9])
# plt.show()

#* color
# plt.bar(x,y,width=[0.5,0.7,0.9], color=['red', 'green', "cyan"])
# plt.show()

#* align

plt.bar(x,y,width=[1.2,2.0,1.2], color='black',align='edge')
plt.xlabel('pandi')
plt.ylabel('haklaYash')
plt.title('nigga')

plt.show()