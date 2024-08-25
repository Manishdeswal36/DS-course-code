import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)# 1 row 1 column 1figure number
ax.set(
    xlim = [0.5,4.5],
    ylim = [-2,8],
    title = 'an example axes',
    xlabel = 'X-axis',
    ylabel = 'Y-axis'
)
plt.show()