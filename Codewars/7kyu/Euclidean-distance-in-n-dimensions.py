"""
    Implement a function to calculate the distance between two points in n-dimensional space. 
    The two points will be passed to your function as arrays of the same length.

    Round your answers to two decimal places."
"""
import math

def euclidean_distance(point1, point2):
    result = 0
    for i in range(len(point1)):
        result += pow(point2[i] - point1[i], 2)
    
    return round(math.sqrt(result) , 2)
