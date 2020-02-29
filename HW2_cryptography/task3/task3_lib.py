import string

def double_point(point_x, point_y):
    #calculate the slope numerator
    s1 = ( 3*(point_x**2) + 2 ) % 17
    #calculate the slope denominator
    s2 = modular_inverse(2*point_y)

    s = (s1 * s2) % 17

    #calculate the x coordinate
    doubled_x = ((s**2)% 17) - (2*(point_x)%17)
    #calculate the y coordinate
    doubled_y = (s*(point_x - doubled_x)%17) - (point_y%17)

    doubled_point = [doubled_x, doubled_y]
    return doubled_point

def addition(p_x, p_y, q_x, q_y):
    #calculate the slope
    s1 = (p_y - q_y)%17 
    s2 = modular_inverse(p_x - q_x)

    s = (s1 * s2) %17
    #calculate the x coordinate
    added_x = (((s**2)%17) - ((p_x + q_x)%17))%17
    #calculate the y coordinate
    added_y = ((s*(p_x - added_x)%17) - p_y)%17

    added_point = [added_x, added_y]
    return added_point

def modular_inverse(n):
    m = 0
    while (m * n) % 17 != 1:
        m += 1

    return m

def scalar_multiply(point_x, point_y, scalar_k):

    #use k % n (order of G)
    k = scalar_k % 19

    point = [point_x, point_y]
    multiplied_point = [0,0]

    if k == 1:
        return point

    for i in range(k-1):
        if i == 0:
            multiplied_point = double_point(point[0], point[1])
        else:
            multiplied_point = addition(multiplied_point[0], multiplied_point[1], point[0], point[1])

    return multiplied_point

if __name__ == "__main__":
    print("main called from task1_lib.py")
