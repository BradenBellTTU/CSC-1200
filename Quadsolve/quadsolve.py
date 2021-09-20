import math

print("X = -b +- sqrt(b^2-4(a)(c))")
print("   -------------------------")
print("              2(a)")

a = float(input("\na: "))
b = float(input("\nb: "))
c = float(input("\nc: "))

x = ((-b) + math.sqrt((b ** 2) - (4 * a * c)))
y = -b - math.sqrt((b ** 2) - (4 * a * c))

print(x)
print(y)