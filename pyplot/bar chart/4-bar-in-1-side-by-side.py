import matplotlib.pyplot as plt
import numpy as np

info= ['gold',' silver', 'bronze', 'Total']
australia = [80, 59, 59, 198]
India= [26, 20, 20,66]
england=[45,45,46,136]
canada=[15,40,27,82]
x=np.arange(len(info))

plt.bar(x, australia,width=0.15, color='pink', label =" by Australia")
plt.bar(x+0.15, India,width=0.15,color='gold', label=" by India")
plt.bar(x+0.30, england,width=0.15,color='cyan', label=" by England")
plt.bar(x+0.45, canada,width=0.15,color='silver', label=" by Canada")
plt.xlabel ("Medals")
plt.ylabel ("Amount")
plt.legend()
plt.title ("Amount of Medals won by India ,Australia,england,canada in a cricket Tournament")
#* ticks
plt.xticks(x+0.225,info)
plt.show() 
