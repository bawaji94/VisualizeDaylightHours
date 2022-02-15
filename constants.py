import numpy as np
from utils import Latitude

LATITUDES = np.arange(-90, 91)[::-1]
DAYS = np.arange(1, 366)

SPECIAL_LATITUDES = [
    Latitude('Arctic Circle', 66.57, 'black'),
    Latitude('Tropic of Cancer', 23.5, 'blue'),
    Latitude('Equator', 0, 'red'),
    Latitude('Tropic of Capricorn', -23.5, 'blue'),
    Latitude('Antartic Circle', -66.57, 'black'),
]

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
MONTH_END_DAYS = np.array([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365])
MID_MONTH_DAYS = (MONTH_END_DAYS[1:] + MONTH_END_DAYS[:-1])/2