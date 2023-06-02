import matplotlib.pyplot as plt
import numpy as np
import rasterio
import scipy.stats as stats
from matplotlib.colors import ListedColormap
from rasterio.plot import show
from rasterio.windows import from_bounds


def clipping_img(src, tar):
    # Open the GeoTIFF file
    with rasterio.open(src) as src:
        # Get the window indices
        window = from_bounds(min_lon, min_lat, max_lon, max_lat, src.transform)

        # Read the data for the window
        data = src.read(window=window)

        # Create a new GeoTIFF file
        profile = src.profile.copy()
        profile.update({
            'height': window.height,
            'width': window.width,
            'transform': src.window_transform(window)
        })
        with rasterio.open(tar, 'w', **profile) as dst:
            # Write the data to the new GeoTIFF file
            dst.write(data)


def decorate_fig(tar):
    # Open the GeoTIFF file
    with rasterio.open(tar) as src:
        # Read the data
        data = src.read()

        # Get the spatial reference system and transform
        crs = src.crs
        transform = src.transform

        # Get the x and y coordinates of the corners
        xmin, ymin, xmax, ymax = src.bounds
        x = [xmin, xmax]
        y = [ymin, ymax]

        # Get the colormap and normalize the data
        # cmap = ListedColormap(['black', 'gray', "white", 'green', 'blue', "purple", "yellow", "orange", 'red'])
        """cmap = ListedColormap(
            [[97 / 255, 97 / 255, 97 / 255], [99 / 255, 96 / 255, 95 / 255], [101 / 255, 95 / 255, 94 / 255],
             [102 / 255, 94 / 255, 92 / 255], [104 / 255, 93 / 255, 91 / 255], [106 / 255, 92 / 255, 89 / 255],
             [107 / 255, 91 / 255, 88 / 255], [109 / 255, 90 / 255, 86 / 255], [111 / 255, 89 / 255, 85 / 255],
             [112 / 255, 88 / 255, 83 / 255], [114 / 255, 87 / 255, 82 / 255], [115 / 255, 86 / 255, 80 / 255],
             [116 / 255, 85 / 255, 79 / 255], [118 / 255, 84 / 255, 77 / 255], [119 / 255, 83 / 255, 76 / 255],
             [120 / 255, 82 / 255, 74 / 255], [122 / 255, 81 / 255, 73 / 255], [123 / 255, 80 / 255, 71 / 255],
             [124 / 255, 79 / 255, 70 / 255], [125 / 255, 78 / 255, 68 / 255], [126 / 255, 77 / 255, 67 / 255],
             [128 / 255, 76 / 255, 65 / 255], [129 / 255, 75 / 255, 64 / 255], [130 / 255, 73 / 255, 62 / 255],
             [131 / 255, 72 / 255, 61 / 255], [132 / 255, 71 / 255, 60 / 255], [133 / 255, 70 / 255, 58 / 255],
             [134 / 255, 69 / 255, 57 / 255], [135 / 255, 67 / 255, 55 / 255], [136 / 255, 66 / 255, 54 / 255],
             [137 / 255, 65 / 255, 52 / 255], [138 / 255, 64 / 255, 51 / 255], [139 / 255, 62 / 255, 49 / 255],
             [140 / 255, 61 / 255, 48 / 255], [141 / 255, 59 / 255, 46 / 255], [142 / 255, 58 / 255, 45 / 255],
             [142 / 255, 57 / 255, 43 / 255], [143 / 255, 55 / 255, 42 / 255], [144 / 255, 54 / 255, 40 / 255],
             [145 / 255, 52 / 255, 39 / 255]])
        """
        cmap = ListedColormap([[c, c, c] for c in np.linspace(0, 1, 500)])
        norm = plt.Normalize(vmin=0, vmax=4)

    # Create a figure and plot the data
    fig, ax = plt.subplots(figsize=(10, 10))

    # Set the x and y ticks to be spaced every 0.5 degrees
    ax.set_xticks(np.around(np.linspace(start=xmin, stop=xmax, num=15), 4))
    ax.set_yticks(np.around(np.linspace(start=ymin, stop=ymax, num=15), 4))
    ax.tick_params(axis='x', labelrotation=60)

    # Set the tick labels for the x and y ticks
    # ax.set_xticklabels([str(i) for i in range(-180, 181, 10)])
    # ax.set_yticklabels([str(i) for i in range(-90, 91, 10)])

    show(data, ax=ax, cmap=cmap, transform=transform)

    # Add gridlines for longitude and latitude
    ax.grid(color='black', linestyle='--', linewidth=0.5)

    # Add labels for the gridlines
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    # Show the plot
    plt.show()
    return fig


def save_fig(img):
    img.savefig(tar_file_name + ".png")


if __name__ == '__main__':
    # -180W, +180E, +75N, -65S
    positions = {"New York, New York": [40.7128, -74.0060], "Los Angeles, California": [34.0522, -118.2437],
                 "Chicago, Illinois": [41.8781, -87.6298], "Houston, Texas": [29.7604, -95.3698],
                 "Phoenix, Arizona": [33.4484, -112.0740], "Philadelphia, Pennsylvania": [39.9526, -75.1652],
                 "San Antonio, Texas": [29.4241, -98.4936], "San Diego, California": [32.7157, -117.1611],
                 "Dallas, Texas": [32.7767, -96.7970], "San Jose, California": [37.3382, -121.8863],
                 "Austin, Texas": [30.2672, -97.7431], "Jacksonville, Florida": [30.3322, -81.6557],
                 "Fort Worth, Texas": [32.7555, -97.3308], "Columbus, Ohio": [39.9612, -82.9988],
                 "San Francisco, California": [37.7749, -122.4194], "Charlotte, North Carolina": [35.2271, -80.8431],
                 "Indianapolis, Indiana": [39.7684, -86.1581], "Seattle, Washington": [47.6062, -122.3321],
                 "Denver, Colorado": [39.7392, -104.9903], "Washington, District of Columbia": [38.9072, -77.0369]}

    # {"Tucson Arizona": [32.2226, -110.9747], "Flagstaff Arizona": [35.1981, -111.6513],"New York City (NYC)": [40.7128, -74.0060], "Los Angeles": [34.0522, -118.2437]}
    for city_name, pos in zip(positions.keys(), positions.keys()):
        for year in range(2013, 2021):
            src_file_name = f"../data/VNL_v21_npp_{year}_global_vcmslcfg_c202205302300.average_masked.dat.tif"
            min_lat, max_lat = positions[pos][0] - 0.3, positions[pos][0] + 0.3
            min_lon, max_lon = positions[pos][1] - 0.3, positions[pos][1] + 0.3
            # print(city_name, np.around([min_lat, max_lat, min_lon, max_lon], 4))
            tar_file_name = f"../data/compare_maps/{city_name}-{year}-img.tiff"

            clipping_img(src_file_name, tar_file_name)
            # decorate_fig()
            save_fig(decorate_fig(tar_file_name))

            # Open file
            with rasterio.open(tar_file_name) as src:
                # Read data as numpy array
                data = src.read(1)
                # Calculate statistics
                means = (np.mean(data))
                medians = (np.median(data))
                modes = (float(stats.mode(data, axis=None)[0]))
                variances = (np.var(data))
                stds = (np.std(data))
                print(f"{city_name},{year},{means},{medians},{modes},{variances},{stds}")

"""
    city_name = "LA"
    min_lon, max_lon = -118.8, -117.4
    min_lat, max_lat = 33.4, 34.4
    city_name = "1-BIBE-TX"
    min_lat, max_lat = 29.0862, 29.4272
    min_lon, max_lon = -103.5939, -103.0358
    city_name = "2-FRBG-TX"
    min_lat, max_lat = 30.2013, 30.3223
    min_lon, max_lon = -98.9926, -98.7526
    city_name = "3-RORO-TX"
    min_lat, max_lat = 30.4646, 30.6256
    min_lon, max_lon = -97.7647, -97.5420
    city_name = "4-HOU-TX"
    min_lat, max_lat = 29.5264, 30.1109
    min_lon, max_lon = -95.6473, -95.0235
    city_name = "1-EVER-FL"
    min_lat, max_lat = 25.0957, 25.8767
    min_lon, max_lon = -81.4220, -80.5172
    city_name = "2-ARCA-FL"
    min_lat, max_lat = 27.1286, 27.2809
    min_lon, max_lon = -81.8966, -81.7378
    city_name = "3-WEST-FL"
    min_lat, max_lat = 26.0632, 26.1728
    min_lon, max_lon = -80.4256, -80.2819
    city_name = "4-MIA-FL"
    min_lat, max_lat = 25.7617, 25.9086
    min_lon, max_lon = -80.3207, -80.1304
    """
