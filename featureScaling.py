def featureScaling(arr):
    if len(arr) <= 0:
        return None
    minValue = arr[0]
    maxValue = arr[0]
    for each in arr:
        if each < minValue:
            minValue = each
        if each > maxValue:
            maxValue = each
    if minValue == maxValue:
        return [1 for x in arr]
    return [(x - minValue) * 1.0 / (maxValue - minValue) for x in arr]

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

data = [1, 1, 1, 1]
print featureScaling(data)

from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
resaled_weight = scaler.fit_transform(weights)

print scaler.data_min_, scaler.data_max_, scaler.data_range_
print resaled_weight