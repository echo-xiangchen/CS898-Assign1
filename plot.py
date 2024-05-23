import numpy as np
import matplotlib.pyplot as plt

file_path = 'A1-Chen-054.txt'

# Load the data from the file
data = np.loadtxt(file_path, delimiter=',')

# Initialize a dictionary to store unique x-values with their first corresponding y-value
unique_data = {}
for x, y in data:
    if x not in unique_data:
        unique_data[x] = y

# Convert the dictionary back to two lists for plotting
x_values = list(unique_data.keys())
y_values = list(unique_data.values())

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Reflectance data for a snowpack', color='red')
plt.title('CS898 Assignment 1 Captured Curve - Xiang Chen - 20892054')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance (%)')
plt.grid(True)
plt.legend()

# Set the limits for x and y axes
plt.xlim(350, 2500)
plt.ylim(0, 100)

# Save the plot as a PNG file
plt.savefig('A1-Chen-054.png')

# Show the plot
plt.show()

