import math

def find_roots(a, b, c):
    """
    Description:function takes coefficient of quadratic equation and return roots of quadratic equation
    Parameter:coefficient of quadratic equation
    Return:roots of quadratic equation
    """
    delta = b**2 - 4*a*c

    if delta < 0:
        return None, None  # No real roots
    elif delta == 0:
        root = -b / (2 * a)
        return root, root  # One real root 
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return root1, root2  # Two distinct real roots
    
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

root1, root2 = find_roots(a, b, c)

if root1 is None and root2 is None:
    print("The equation has no real roots.")
elif root1 == root2:
    print(f"The equation has one real root: {root1}")
else:
    print(f"The equation has two real roots: {root1} and {root2}")


# import math

# def find_roots(a, b, c):
#     delta = b**2 - 4*a*c

#     if delta < 0:
#         print("The equation has no real roots.")
#         # return None, None  # No real roots
#     elif delta == 0:
#         root = -b / (2 * a)
#         print(f"The equation has one real root: {root}")
#         # return root, root  # One real root 
#     else:
#         root1 = (-b + math.sqrt(delta)) / (2 * a)
#         root2 = (-b - math.sqrt(delta)) / (2 * a)
#         print(f"The equation has two real roots: {root1} and {root2}")
#         # return root1, root2  # Two distinct real roots
    
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))

# find_roots(a, b, c)

