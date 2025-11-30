import matplotlib.pyplot as plt


medals = ['gold',' silver', 'bronze', 'Total']
australia = [80, 59, 59, 198]
India= [26, 20, 20,66]

plt.bar (medals, australia,color='pink', label =" by Australia")
plt.bar (medals, India,color='yellow', label=" by India")
plt.xlabel ("Medals")
plt.ylabel ("Amount")
plt.legend()
plt.title ("Amount of Medals won by India & Australia in a cricket Tournament")
plt.show() 
