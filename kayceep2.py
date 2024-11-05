import matplotlib.pyplot as plt
import numpy as np 
import random

# generate random blood sugar level
bsl = [random.randint(80, 150) for _ in range (100)]

# define blood sugar ranges (bins)
bins = [80, 100, 125, 150]

# count patients in each bin
bin_counts = [
    len([x for x in bsl if 80<= x <100]),
    len([x for x in bsl if 100<= x <125]),
    len([x for x in bsl if 125<= x <150])
]

# create histrogram
x = np.arrange(3)
width = 0.98
plt.bar(x, bin_counts, width, color=['red', 'yellow', 'blue'])

# format plot
plt.xticks(x, ['80-100', '100-125', '125-150'])
plt.xlabel('blood sugar range (mg/dl)')
plt.ylabel('number of patients')
plt.title('distibution of blood sugar levels')

# add legend 
plt.legend(['80-100 (red)', '100-125 (yellow)', '125-150 (blue)'])

plt.show()