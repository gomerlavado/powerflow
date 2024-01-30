import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

omega = 2 * math.pi * 60
time = np.linspace(0, 0.1, 1000)

irms = 1
im = math.sqrt(2) * irms
thetai = math.radians(30)

l = 0.5
z = complex(0, omega*l)

it = im * np.cos(omega * time + thetai)
vt = - math.sqrt(2) * omega * l * irms * np.sin(omega * time + thetai)

s = z * irms**2

q = s.imag
print(q)

plt.plot(time, vt*it, "orange", time, it, "tab:green", time, vt, "tab:blue")
plt.hlines(q, 0, 0.1, colors="orange", linestyles="dashed")
plt.show()

vrms = 220
vm = math.sqrt(2) * vrms
thetav = math.radians(60)

c = 0.0005
z = complex(0, -1/(omega*c))

vt = vm * np.cos(omega * time + thetav)
it = - math.sqrt(2) * omega * c * vrms * np.sin(omega * time + thetav)

s = vrms ** 2 / z.conjugate()
q = s.imag
print(q)

plt.plot(time, vt*it, "orange", time, it, "tab:green", time, vt, "tab:blue")
plt.hlines(q, 0, 0.1, colors="orange", linestyles="dashed")
plt.show()
