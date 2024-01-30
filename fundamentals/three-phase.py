import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

vrms = 220
irms = 1

vm = math.sqrt(2) * vrms
thetav = math.radians(0)
diff = math.radians(120)
omega = 2 * math.pi * 60
time = np.linspace(0, 0.1, 1000)

va = vm * np.cos(omega * time + thetav)
vb = vm * np.cos(omega * time + thetav - diff)
vc = vm * np.cos(omega * time + thetav + diff)

ean = ax.plot(time[0], va[0], label="Ean")[0]
ebn = ax.plot(time[0], vb[0], label="Ebn")[0]
ecn = ax.plot(time[0], vc[0], label="Ecn")[0]

ax.set(xlim=[0, 0.02], ylim=[-600, 600], xlabel="Time [s]", ylabel="Voltage [V]")
ax.legend()

def update(frame):
    ean.set_xdata(time[:frame])
    ean.set_ydata(va[:frame])

    ebn.set_xdata(time[:frame])
    ebn.set_ydata(vb[:frame])

    ecn.set_xdata(time[:frame])
    ecn.set_ydata(vc[:frame])

    return (ean, ebn, ecn)

plt.grid(color="gray", linestyle="dotted")

ani = animation.FuncAnimation(fig=fig, func=update, frames=200, interval=50)
plt.show()

"""
it can be observed that the voltages reach their maximum
values in the order abc, so we say the phase
sequence is an abc or positive sequence.
"""
