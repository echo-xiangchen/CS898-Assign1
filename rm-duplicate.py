import numpy as np

input_file_path = 'A1-Chen-054-ori.txt'
output_file_path = 'A1-Chen-054.txt'

# Load the data from the file
data = np.loadtxt(input_file_path, delimiter=',')

# Initialize a dictionary to store x-values with all corresponding y-values
data_dict = {}
for x, y in data:
    if x in data_dict:
        data_dict[x].append(y)
    else:
        data_dict[x] = [y]

# Calculate the average of y-values for each unique x-value
averaged_data = {x: np.mean(ys) for x, ys in data_dict.items()}

# Write the averaged data to a new text file
with open(output_file_path, 'w') as file:
    for x, avg_y in averaged_data.items():
        file.write(f"{x},{avg_y}\n")

print(f"Averaged data saved to {output_file_path}")

