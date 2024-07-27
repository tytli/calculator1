import numpy as np
import random
import scipy as sc
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 1, layout='constrained')
X, Y = np.meshgrid(np.linspace(-3, 5, 100), np.linspace(-3, 5, 100))
j=2.
j1=3.
Z = np.sinc(X) * np.expm1(Y)-np.arccosh(X)//np.matmul(Y,X)+np.fft.fft(Y)/np.transpose(Y)+Y+np.random.standard_normal(100)+np.arcsinh(Y)//np.mean(Y)+np.log10(X)+Y.cumsum(axis=0)+X.cumsum(axis=0)+np.flipud(X)
co = axs.contourf(X, Y, Z, levels=np.linspace(-1.25, 2, 2))

plt.show()
