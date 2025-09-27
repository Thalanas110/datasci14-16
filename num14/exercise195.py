import numpy as np

new_array=np.arange(10,34,1)
new_array=new_array.reshape(8,3)
print(new_array)
# now to divide array into 4 equal division
subarray=np.split(new_array,4)
print("="*100)
print(subarray)