import math

import numpy as np


def surface_area(lat1, lon1, lat2, lon2):
    R = 6371  # mean radius of Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return (R ** 2 * c) / 2


# BIBE-TX
BIBE_lat = 29.25
BIBE_long = -103.25
# FRBG-TX
FRBG_lat = 30.2765
FRBG_long = -98.8714
# RORO-TX
RORO_lat = 30.5083
RORO_long = -97.6789
# HOU-TX
HOU_lat = 29.7604
HOU_long = -95.3698
# EVER-FL
EVER_lat = 25.2867
EVER_long = -80.8987
# ARCA-FL
ARCA_lat = 27.22
ARCA_long = -81.8586
# WEST-FL
WEST_lat = 26.0998
WEST_long = -80.395
# MIA-FL
MIA_lat = 25.7617
MIA_long = -80.1918
cities = ["1-BIBE-TX", "2-FRBG-TX", "3-RORO-TX", "4-HOU-TX", "1-EVER-FL", "2-ARCA-FL", "3-WEST-FL", "4-MIA-FL"]
positions = {"BIBE": [BIBE_lat, BIBE_long], "FRBG": [FRBG_lat, FRBG_long], "RORO": [RORO_lat, RORO_long],
             "HOU": [HOU_lat, HOU_long], "EVER": [EVER_lat, EVER_long], "ARCA": [ARCA_lat, ARCA_long],
             "WEST": [WEST_lat, WEST_long], "MIA": [MIA_lat, MIA_long]}
areas = []
for city_name, pos in zip(cities, positions.keys()):
    min_lat, max_lat = positions[pos][0] - 0.03, positions[pos][0] + 0.03
    min_lon, max_lon = positions[pos][1] - 0.03, positions[pos][1] + 0.03
    area = surface_area(min_lat, min_lon, max_lat, max_lon)
    areas.append(area)
    print(pos, ":", area)

print("std:", np.std(areas))
print("mean:", np.mean(areas))
