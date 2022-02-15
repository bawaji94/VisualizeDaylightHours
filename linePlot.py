import numpy as np
import matplotlib.pyplot as plt
from utils import Daylight
from constants import MID_MONTH_DAYS, DAYS, MONTHS, SPECIAL_LATITUDES

OUTPUT_PATH = '/home/e4r/Documents/shabbir'
plt.figure(figsize=(13, 7.5))
for special_latitude in SPECIAL_LATITUDES:
    daylight_for_latitude = Daylight(special_latitude.latitude, DAYS)
    plt.plot(DAYS, daylight_for_latitude, label=str(special_latitude), linewidth=3)

plt.legend(fontsize=14, loc=(0.59, 0.76))
plt.xlim(0, 365)
plt.ylim(0, 24.5)
plt.yticks([0, 12, 24, 3, 6, 9, 15, 18, 21], fontsize=13)
plt.grid()
plt.xticks(MID_MONTH_DAYS, MONTHS, fontsize=13)
plt.xlabel('Months', fontsize=16)
plt.ylabel('Hours of Daylight per day', fontsize=16)
plt.tight_layout()
plt.savefig(f'{OUTPUT_PATH}/linePlotHoursOfDaylightperDay.png')
plt.show()