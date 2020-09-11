import numpy as np
import matplotlib.pyplot as plt
import nanonispy as nap


filepath = r'C:\data\TBAVSe2\TBA-VSe2 LHe\Bias-Spectroscopy00001.dat'
example = nap.read.Spec(filepath)
"""
print(example.header.keys())
for i in example.header.keys():
    print(i)
    print(example.header.get(i))
"""
for i in example.signals.keys():
    print(i)
    print(example.signals.get(i))

x = example.signals.get('Bias calc (V)')
y_current = example.signals.get('Current (A)')
y_didv = example.signals.get('LI Demod 1 X (A)')
print(x)
print(y_didv)
fig,ax = plt.subplots(figsize=(5,5))
ax.plot(x,y_didv)
plt.show()