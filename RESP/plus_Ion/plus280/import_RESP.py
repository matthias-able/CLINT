import numpy as np

# Read the contents of the file
with open('qout_stage2', 'r') as file:
    data = file.read()

# Split the data by whitespace to extract individual numbers
numbers = [float(num) for num in data.split()]

# Convert the list of numbers into a NumPy array
np_array = np.array(numbers)

# Print or work with the NumPy array
print(np_array)