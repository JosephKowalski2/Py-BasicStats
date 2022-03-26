from typing import List
import math


def zcount(data: List[float]) -> float:
    return float(len(data))

def zmean(data: List[float]) -> float:
    return sum(data) / zcount(data)

def zmode(data: List[float]) -> float:
    return max(set(data), key=data.count)

def zmedian(data: List[float]) -> float:
    sorted_list = sorted(data)
    index = (len(data) - 1) // 2
    if len(data) % 2:
        return sorted_list[index]
    else:
        return (sorted_list[index] + sorted_list[index + 1]) / 2.0

def zvariance(data: List[float]) -> float:
    n = zcount(data) - 1
    mean = sum(data) / n
    deviations = []
    for x in data:
        deviations.append(abs(mean - x) ** 2)
    return sum(deviations) / n

def zstddev(data: List[float]) -> float:
    return math.sqrt(zvariance(data))

def zstderr(data: List[float]) -> float:
    return zstddev(data) / zcount(data)

def zcorr(datax: List[float], datay: List[float]) -> float:
    return cov(datax, datay) / (zstddev(datax) * zstddev(datay))

def cov(datax: List[float], datay: List[float]) -> float:
    sum = 0
    if zcount(datax) == zcount(datay):
        for i in range(len(datax)):
            sum += ((datax[i] - zmean(datax)) * (datay[i] - zmean(datay)))
    return sum / (zcount(datax) - 1)

def readDataFile(file):
    setA, setB = [], []
    with open(file) as f:
        next_line = f.readline()
        for line in f:
            row = line.split(',')
            setA.append(float(row[0]))
            setB.append(float(row[1]))
    return setA, setB

def readDataSets(files):
    data = {}
    for file in files:
        csvs = readDataFile(file)
        data[file] = csvs
    return data