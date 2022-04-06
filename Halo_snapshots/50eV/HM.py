import numpy as np
import matplotlib.pyplot as plt

# Data entry
a050 = np.loadtxt("snapshot_a=0.50_halos")
a100 = np.loadtxt("snapshot_a=1.00_halos")



# Unpacking mass [2], radii [5]

# for a=100

#for i in range(0,len(a100[:,0])):
 #       print("haloID: ",a100[:,0][i], "Mass: ", a100[:,2][i], "radii: ", a100[:,5][i])


# determening nr of masses under m

def mass_counter(data, mass):
    counter = 0
    for item in data:
        if item <= mass:
            counter += 1        
    return counter

minM = min(a100[:,2])
maxM = max(a100[:,2])
print(minM, maxM)
ms = np.linspace(minM, maxM,10000)

counts100 = []
counts050 = []
for mass in ms:
    c100 = mass_counter(np.log10(a100[:,2]), np.log10(mass))
    c050 = mass_counter(np.log10(a050[:,2]), np.log10(mass))
    counts100.append(c100)
    counts050.append(c050)
    #print("mass: ", mass, "count a=1.00: ",c100)


#//making derivative??
dN100=[]
for i in range(0,len(counts100)):
    dN = counts100[i]-counts100[-1]
# plotting yayyyyyy!

der100 = np.gradient(np.log10(counts100),np.log10(ms))
der050 = np.gradient(np.log10(counts050),np.log10(ms))
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(20,7))

plt.suptitle("50eV HM-function")

ax[0].plot(np.log10(ms), np.log10(counts100), label = "a=1.00", c = "k")
ax[0].plot(np.log10(ms), np.log10(counts050), label = "a=0.50",ls = "--", c="k")


ax[1].plot(np.log10(ms), der100, label = "dN, a=1.00")
ax[1].plot(np.log10(ms), der050, label = "dN, a=0.50")


for plt in [ax[0],ax[1]]:
    plt.legend()
    plt.set_xlabel("log(m)")
ax[0].set_ylabel("log(N)")
ax[1].set_ylabel("dN")
fig.savefig("50eV_MH.png")









