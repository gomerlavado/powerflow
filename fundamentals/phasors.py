import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

# Single phase system
vrms = 220
irms = 1
# max voltage and current
vm = math.sqrt(2) * vrms
im = math.sqrt(2) * irms
thetav = math.radians(60)
thetai = math.radians(30)
omega = 2 * math.pi * 60
time = np.linspace(0, 0.1, 1000)

vt = vm * np.cos(omega * time + thetav)
it = im * np.cos(omega * time + thetai)

plt.plot(time, vt, "orange", time, it, "tab:green", time, vt*it, "tab:blue")
plt.hlines(220, 0, 0.1, colors="orange", linestyles="dashed")
plt.show()

phi = thetav - thetai
pavg = vrms * irms * math.cos(phi)
print(pavg)

vz = complex(vrms * math.cos(thetav), vrms * math.sin(thetav))
iz = complex(irms * math.cos(thetai), irms * math.sin(thetai))

s = vz * iz.conjugate()
print(s)
print(s.real)
print(cmath.polar(s))

pf = math.cos(phi)
print(math.acos(pf))
