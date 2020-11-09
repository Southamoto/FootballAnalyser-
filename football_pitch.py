import matplotlib.pyplot as plt
from matplotlib.patches import Arc

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot([0, 0], [0, 90], color="blue")
plt.plot([0, 130], [90, 90], color="orange")
plt.plot([130, 130], [90, 0], color="green")
plt.plot([130, 0], [0, 0], color="red")
plt.plot([65, 65], [0, 90], color="pink")

plt.show()
