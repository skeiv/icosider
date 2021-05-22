import bpy
from math import sqrt

#a = length of edge
a = 2
r=sqrt(2*(5+sqrt(5))) / 4 * a
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=r, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
