# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  This script finds the intersection point (if it exists) between a ray and Earth reference ellipsoid
# Parameters:
#  d_l_x: x-component of origin-referenced ray direction
#  d_l_y: y-component of origin-referenced ray direction
#  d_l_z: z-component of origin-referenced ray direction
#  c_l_x: x-component offset of ray origin
#  c_l_y: y-component offset of ray origin
#  c_l_z: z-component offset of ray origin

# Output:
#  Prints the x-component of the intersection point, y-component of the inersection point, z-component of the intersection point
#
# Written by Kristin Eickelbeck
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions

## scalar multiplication
def smul(s,v):
    sprod = []
    for i in range(0,len(v)):
        sprod.append(s*v[i])
    return sprod

## vector addition
def add(v1,v2):
    if len(v1) != len(v2):
        return None
    else:
        v3 = []
        for i in range(0,len(v1)):
            v3.append(v1[i]+v2[i])
    return v3

# initialize script arguments
d_l_x = float('nan') # x-component of origin-referenced ray direction
d_l_y = float('nan') # y-component of origin-referenced ray direction
d_l_z = float('nan') # z-component of origin-referenced ray direction
c_l_x = float('nan') # x-component offset of ray origin
c_l_y = float('nan') # y-component offset of ray origin
c_l_z = float('nan') # z-component offset of ray origin

# parse script arguments
if len(sys.argv)==7:
   d_l_x = float(sys.argv[1]) # x-component of origin-referenced ray direction
   d_l_y = float(sys.argv[2]) # y-component of origin-referenced ray direction
   d_l_z = float(sys.argv[3]) # z-component of origin-referenced ray direction
   c_l_x = float(sys.argv[4]) # x-component offset of ray origin
   c_l_y = float(sys.argv[5])# y-component offset of ray origin
   c_l_z = float(sys.argv[6]) # z-component offset of ray origin
else:
   print(\
    'Usage: '\
    'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
   )
   exit()

# write script below this line

a = d_l_x**2 + d_l_y**2 + (d_l_z**2)/(1 - E_E**2)
b = 2*(d_l_x*c_l_x + d_l_y*c_l_y + d_l_z*c_l_z/(1 - E_E**2))
c = c_l_x**2 + c_l_y**2 + c_l_z**2/(1-E_E**2) - R_E_KM**2

discr = b*b-4.0*a*c

d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]

if discr >=0.0:
    d = (-b-math.sqrt(discr))/(2*a)
    if d<0.0:
        d = (-b+math.sqrt(discr))/(2*a)
    if d>=0.0:
        l_d = add(smul(d,d_l),c_l)
        print(l_d[0]) # x-component of intersection point
        print(l_d[1]) # y-component of intersection point
        print(l_d[2]) # z-component of intersection point




