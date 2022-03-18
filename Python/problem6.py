import numpy as np
nums = np.arange(1, 101)
numssquared = (lambda x:x**2)(nums)
print(nums.sum()**2-numssquared)
