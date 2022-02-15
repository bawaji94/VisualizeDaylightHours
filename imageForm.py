import numpy as np
import matplotlib.pyplot as plt
from utils import Latitude, Daylight
from constants import LATITUDES, MID_MONTH_DAYS, DAYS, MONTHS, SPECIAL_LATITUDES

OUTPUT_PATH = '/home/e4r/Documents/shabbir'
plt.figure(figsize=(13,5.5))
DAY_GRID, LAT_GRID = np.meshgrid(DAYS, LATITUDES)
plt.imshow(Daylight(LAT_GRID, DAY_GRID), extent=[1,365,-90,90])
plt.xticks(MID_MONTH_DAYS, MONTHS, fontsize=14)
latitude_ticks=[-90, -67.5, -45, -22.5 ,0, 22.5, 45, 67.5, 90]
plt.yticks(
    latitude_ticks,
    list(map(Latitude.beautify, latitude_ticks)),
    fontsize=13
)
plt.xlabel('Months', fontsize=16)
plt.ylabel('Latitude', fontsize=16)
for special_latitude in SPECIAL_LATITUDES:
    plt.axhline(special_latitude.latitude, linestyle='--', color=special_latitude.color)
    plt.text(5, special_latitude.latitude+5, str(special_latitude), rotation=0, verticalalignment='center', fontsize=14, color=special_latitude.color)
cbar = plt.colorbar(ticks=[0, 24, 12, 6, 18, 21, 15, 9, 3])
cbar.ax.set_ylabel('Hours of Daylight per day', fontsize=14)
plt.tight_layout()
plt.savefig(f'{OUTPUT_PATH}/imageFormHoursOfDaylightperDay.png')
plt.show()