import os
import re

import matplotlib.pyplot as plt
import numpy as np
import rasterio
import scipy.stats as stats

path = "../data/city_map/"

# Get list of files ending in ".tiff" in the directory
files = [f for f in os.listdir(path) if f.endswith('.tiff')]

# Sort files by year
files = sorted(files, key=lambda x: int(re.findall('\d\d\d\d', x)[0]))

# Define arrays to store data
means = []
medians = []
modes = []
variances = []
stds = []

# Loop through files and calculate statistics
for file in files:
    # Open file
    with rasterio.open(os.path.join(path, file)) as src:
        # Read data as numpy array
        data = src.read(1)

        # Calculate statistics
        means.append(np.mean(data))
        medians.append(np.median(data))
        modes.append(float(stats.mode(data, axis=None)[0]))
        variances.append(np.var(data))
        stds.append(np.std(data))

# Create subplots
fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(8, 16))

# Plot mean data
axes[0].plot(range(2013, 2021), means)
axes[0].set_title('Mean')

# Plot median data
axes[1].plot(range(2013, 2021), medians)
axes[1].set_title('Median')

# Plot mode data
axes[2].plot(range(2013, 2021), modes)
axes[2].set_title('Mode')

# Plot variance data
axes[3].plot(range(2013, 2021), variances)
axes[3].set_title('Variance')

# Plot standard deviation data
axes[4].plot(range(2013, 2021), stds)
axes[4].set_title('Standard Deviation')

# Adjust layout and show plot
fig.tight_layout()
plt.show()

years = range(2013, 2021)
print(f"{'Year':<10} {'Mean':<10} {'Median':<10} {'Mode':<10} {'Variance':<10} {'Std Dev':<10}")
for i, year in enumerate(years):
    print(
        f"{year:<10} {means[i]:<10.2f} {medians[i]:<10.2f} {modes[i][0]:<10.2f} {variances[i]:<10.2f} {stds[i]:<10.2f}")
