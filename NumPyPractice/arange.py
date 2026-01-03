import numpy as np
import time

numpyList = np.arange(10000) # Create a NumPy array with values from 0 to 99
pythonList = list(range(10000)) # Create a standard Python list with values from 0 to 99

# Measure performance of NumPy array by multiplying each element by 2
start = time.perf_counter_ns()
numpyList = numpyList * 2
end = time.perf_counter_ns()
print(f"NumPy array time: {(end - start)} nanoseconds")

start = time.perf_counter_ns()
pythonList = [x * 2 for x in pythonList]

end = time.perf_counter_ns()
print(f"Python list time: {(end - start)} nanoseconds")