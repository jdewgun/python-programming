# -*- coding: utf-8 -*-


def computeDifference(self):
    maxElement = max(self.__elements)
    minElement = min(self.__elements)
    self.maximumDifference = abs(maxElement - minElement)
