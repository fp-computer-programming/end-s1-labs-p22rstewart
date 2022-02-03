# Author RTS 1/28/22

def is_triangle(a, b, c): # Naming variable 
    if ((a < b + c) and (b < a + c) and (c < a + b)) == True: # checking to see if it is a triangle
        return True # confirms it is a triangle
    else: # if not a triangle...
        return False # return false

print(is_triangle(1, 2, 2) == True)
print(is_triangle(7, 20, 2) == False)
print(is_triangle(80, 1, 1) == False)