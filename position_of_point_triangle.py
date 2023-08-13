def equation_of_line(x1, y1, x2, y2):
    # Check if the denominator is zero to avoid division by zero
    if x2 - x1 == 0:
        return None, None

    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)

    # Calculate the y-intercept (b)
    b = y1 - m * x1

    return m, b


# Input: Three distinct points for the triangle
x1, y1 = map(float, input("Enter the 1st coordinates (x,y) of Triangle: ").split())
x2, y2 = map(float, input("Enter the 2nd coordinates (x,y) of Triangle: ").split())
x3, y3 = map(float, input("Enter the 3rd coordinates (x,y) of Triangle: ").split())
a, b = map(float, input("Enter the coordinates (x,y) of Point: ").split())

print("Your Triangle Points:\n 1st point: {}\n 2nd Point: {}\n 3rd Point: {}".format((x1, y1), (x2, y2), (x3, y3)))
print("Your Point is: {}".format((a, b)))

# Checking if the points form a triangle
import numpy as np

p = np.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
q = np.sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2))
r = np.sqrt(pow((x3 - x1), 2) + pow((y3 - y1), 2))

if p + q > r and q + r > p and p + r > q:
    print("Yes, it is a Triangle...")
else:
    print("Not a triangle")

# Calculate the equations of lines for the sides of the triangle
slopes = []
y_intercepts = []
s, y = equation_of_line(x1, y1, x2, y2)
slopes.append(s)
y_intercepts.append(y)
s, y = equation_of_line(x2, y2, x3, y3)
slopes.append(s)
y_intercepts.append(y)
s, y = equation_of_line(x3, y3, x1, y1)
slopes.append(s)
y_intercepts.append(y)
area_tri  = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y2-y1))/2
area_tri1 = abs(x1*(y3-b)+x3*(b-y1)+a*(y1-y3))/2
area_tri2 = abs(x1*(y2-b)+x2*(b-y1)+a*(y1-y2))/2
area_tri3 = abs(x3*(y2-b)+x2*(b-y3)+a*(y3-y2))/2

# Check if the point lies on any of the lines
on_line = False
for i in range(3):
    if slopes[i] is not None and b == slopes[i] * a + y_intercepts[i]:
        on_line = True
        break

if on_line:
    print(f"The point ({a},{b}) lies on the Triangle.")
elif area_tri== area_tri1+area_tri2+area_tri3:
    print(f"Point ({a},{b}) is Inside")
else:
    print("The point does not lie on the Triangle.")


