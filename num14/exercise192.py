import numpy as np

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
#print(sampleArray)
new_array=sampleArray[...,2]
print(new_array)
