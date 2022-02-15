import numpy as np

def Daylight(latitude,day):
    P = np.arcsin(0.39795 * np.cos(0.2163108 + 2 * np.arctan(0.9671396 * np.tan(.00860 * (day - 186)))))
    pi = np.pi
    hm = (np.sin((0.8333 * pi / 180) + np.sin(latitude * pi / 180) * np.sin(P)) / (np.cos(latitude * pi / 180) * np.cos(P)))
    daylightamount = 24 - (24 / pi) * np.arccos(hm)
    daylightamount[np.bitwise_and(np.isnan(daylightamount), hm<0)] = 0
    daylightamount[np.bitwise_and(np.isnan(daylightamount), hm>=0)] = 24
    return daylightamount

class Latitude:
    def __init__(self, name, latitude, color):
        self.name = name
        self.latitude = latitude
        self.color = color
    
    def __str__(self):
        return f'{self.name}({self.beautify(self.latitude)})'

    @staticmethod
    def beautify(l):
        hemisphere = 'N' if l > 0 else 'S'
        if l == 0:
            hemisphere = ''
        return f'{np.abs(l)}°{hemisphere}'