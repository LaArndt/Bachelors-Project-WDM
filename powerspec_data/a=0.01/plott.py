import numpy as np
import matplotlib.pyplot as plt

_50eV = np.loadtxt("powerspec_a=0.01_50eV")
_100eV = np.loadtxt("powerspec_a=0.01_100eV")
_1000eV = np.loadtxt("powerspec_a=0.01_1000eV")
_300eV = np.loadtxt("powerspec_a=0.01_300eV")
_500eV = np.loadtxt("powerspec_a=0.01_500eV")
_10000eV = np.loadtxt("powerspec_a=0.01_10000eV")

figure = plt.figure()
plt.title("matter \n at t=0.01714 Gyr, a=0.01", fontsize=15)

plt.loglog(_50eV[:,0],_50eV[:,2], lw=2,label = "WDM at 50eV")
#plt.loglog(_50eV[:,0],_50eV[:,3], label = "linear component 50eV")

plt.loglog(_100eV[:,0],_100eV[:,2],lw=2, label = "WDM at 100eV")
#plt.loglog(_100eV[:,0],_100eV[:,3], label = "linear component 100eV")

plt.loglog(_300eV[:,0],_300eV[:,2],lw=2, label = "WDM at 300eV")
#plt.loglog(_300eV[:,0],_300eV[:,3], label = "linear component 300eV")

plt.loglog(_500eV[:,0],_500eV[:,2],lw=2, label = "WDM at 500eV")
#plt.loglog(_100eV[:,0],_100eV[:,3], label = "linear component 500eV")

plt.loglog(_1000eV[:,0],_1000eV[:,2],lw=2, label = "WDM at 1000eV")
#plt.loglog(_100eV[:,0],_100eV[:,3], label = "linear component 1000eV")

plt.loglog(_10000eV[:,0],_1000eV[:,2],lw=2, label = "WDM at 10000eV")
#plt.loglog(_100eV[:,0],_100eV[:,3], label = "linear component 10000eV")

plt.legend(loc="lower left")
plt.xlabel("k[Mpc⁻¹]", fontsize=15)
plt.ylabel("power[Mpc³]", fontsize=15)

plt.savefig("powerspectra_a=0.01", format="png")
plt.show()
