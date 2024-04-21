# class Car:
#     def __init__(self,max_speed, speed_unit):
#         self.max_speed = max_speed
#         self.speed_unit = speed_unit
#         print(f"Car with the maximum speed of {max_speed} {speed_unit}")
        

# class Boat:
#     def __init__(self,max_speed):
#         self.max_speed = max_speed
#         print(f"Boat with the maximum speed of {self.max_speed} knots ")

# vehicle = Car(151, "km/h")

# vehicle = Boat(15)


"""
https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true


"""

l1 = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]


# dic = list(dict.fromkeys(l))

# print(dic)


# # def distinct(seq):
# #     return sorted(set(seq), key = seq.index)

def distinct(seq):
    s = set(seq)
    l = []
    for n in seq:
        if n in s:
            l.append(s.remove(n) or n)
    return l


print(distinct(l1))