import math
class Sphere:
    def __init__(self, r=1.0, x=0.0, y=0.0, z=0.0):
        self.r, self.x, self.y, self.z = r, x, y, z
    def get_volume(self):
        volume = 4 / 3.0 * math.pi * self.r ** 3
        return volume 
    def get_square(self):
        square = 4 * math.pi * self.r ** 2
        return square 
    def get_radius(self):
        return self.r
    def get_center(self):
        return (self.x, self.y, self.z)
    def set_radius(self, r):
        self.r = r
    def set_center(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def is_point_inside(self, x, y, z):
        if math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.r:
            return True
        return False

r = int(input("Радиус сферы "))
sx = int(input("Кордината сферы, x:"))
sy = int(input("Кордината сферы, y:"))
sz = int(input("Кордината сферы, z:"))       
sp = Sphere(r, sx, sy, sz)
print("Объем шара = ", sp.get_volume())
print("Площадь внешней поверхности = ", sp.get_square())
print("Радиус сферы = ", sp.get_radius())
print("Координаты центра = ", sp.get_center())

x = int(input("Кордината точки, x:"))
y = int(input("Кордината точки, y:"))
z = int(input("Кордината точки, z:"))
print("Вхождение точки в сферу = ", sp.is_point_inside(x, y, z))
