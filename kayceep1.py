import matplotlib.pyplot as plt
import numpy as np
import random
# generate random blood sugar levels for men and women 
men_bsl = [random.randint(50, 200) for _ in range(15)]
women_bsl = [random.randint(50, 200) for _ in range(15)]

# define blood sugar ranges (bin)
bins = [50, 80, 110, 140, 170, 200]

# create histogram
plt.bar(np.array(15) - 0.04, [men_bsl.count(i) for i in bins],width=0.98, color='green', label = 'men')
plt.bar(np.array(15) - 0.04, [women_bsl.count(i) for i in bins], width=0.98, color='red', label = 'women')

# format plot
plt.xticks(np.arrange(15), ['50-79', '80-109', '110-139', '140-169', '170-199', '200+'])
plt.xlabel('blood sugar range (mg/dl)')
plt.ylabel('number of patients')
plt.title('blood sugar levels of men and women')
plt.legend()

# show plot
plt.show()