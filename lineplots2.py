import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax=plt.axes(projection="3d")
x_data=np.arange(0,50,0.1)
y_data=np.arange(0,50,0.1)
z_data=np.sin(x_data)*np.cos(y_data)
ax.plot(x_data,y_data,z_data)
ax.set_title("Waves")
ax.set_xlabel("X values")
ax.set_ylabel("Y values")
ax.set_zlabel("Z values")
plt.show()
