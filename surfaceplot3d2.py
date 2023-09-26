import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Surface Plots 3d

ax=plt.axes(projection="3d")
x_data=np.arange(-5,5,0.1)
y_data=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x_data,y_data)
Z=np.sin(X)*np.cos(Y)
#print(Z)
ax.plot_surface(X,Y,Z, cmap="plasma")    #adding a color map (higher values are yellow and lower values are purplish)
ax.view_init(azim=0,elev=90)   #to change the default view of the 3d plot
plt.show()


#azimuth=0, elevation of 90
