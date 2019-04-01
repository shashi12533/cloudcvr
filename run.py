import math
import sys


class AirTravel():

    def __init__(self):
        self.radius = 4000
        self.pi = math.pi
        self.maxdist = sys.maxint

    def preprocess(self, latitude, longitude, szcontravel):
        self.latlen = len(latitude)
        self.dist = [[0 for idx in range(szcontravel)] for idy in range(szcontravel)]
        self.lats = [] * len(latitude)
        self.longs = [] * len(latitude)

    def calcdistancebetweenairport(self, lats, longs):
        for idx in range(0, self.latlen):
            for idy in range(0, self.latlen):
                if idx != idy:
                    self.dist[idx][idy] = self.radius * math.acos(
                        math.sin(self.lats[idx]) * math.sin(lats[idy]) + math.cos(lats[idx]) * math.cos(
                            lats[idy]) * math.cos(
                            longs[idx] - longs[idy]))
                else:
                    self.dist[idx][idy] = 0

    def shortesttrip(self, latitude, longitude, cantravel, origin, destination):

        self.preprocess(latitude, longitude, len(cantravel))
        longs = self.longs
        lats = self.lats
        latlen = self.latlen
        dist = self.dist
        for idx in range(0, self.latlen):
            lats.append(latitude[idx] * (self.pi / 180.0))
            longs.append(longitude[idx] * (self.pi / 180.0))

        self.calcdistancebetweenairport(lats, longs)
        for idx in range(0, len(cantravel)):
            airportlink = cantravel[idx].split(" ")
            for idy in range(0, latlen):
                if idx != idy and str(idy) not in airportlink:
                    dist[idx][idy] = self.maxdist
        for idk in range(0, latlen):
            for idx in range(0, latlen):
                for idy in range(0, latlen):
                    dist[idx][idy] = min(dist[idx][idy], dist[idx][idk] + dist[idk][idy])
        if dist[origin][destination] >= self.maxdist:
            return -1

        return dist[origin][destination]


obj = AirTravel()
# print obj.shortesttrip([0, 0, 70], [90, 0, 45], ["1 2", "0 2", "0 1"], 0, 1)
