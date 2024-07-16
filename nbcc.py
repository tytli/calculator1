import numpy as np
import matplotlib.pyplot as plt
import time
fig, ax = plt.subplots()
zc=time.time()
x=np.arange(0,130,30)
y=np.tanh(x)
line,=ax.plot(x,y)
plt.ion()
for delay in np.arange(0,555,0.1):
    y=np.cos(x+delay)
    line.set_ydata(y)



    plt.draw()
    plt.gcf().canvas.flush_events()
    plt.show()
zc1=time.time()
print(zc1-zc)