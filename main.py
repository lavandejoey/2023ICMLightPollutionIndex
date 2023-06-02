import os

import requests

years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
for year in years:
    url = str(f"https://eogdata.mines.edu/nighttime_light/annual/v21/{year}/VNL_v21_npp_{year}_global_vcmcfg_c202205302300.average.dat.tif.gz")
    re = requests.get(url)
    print(re.content)
