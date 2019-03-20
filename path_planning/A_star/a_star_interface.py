import numpy as np
import math
from matplotlib import pyplot as plot
show_animation=False
from a_star_orig import Node
from a_star_orig import calc_index, calc_heuristic, verify_node, calc_obstacle_map, get_motion_model, a_star_planning

def revise_obstacle_coordinates(ox, oy):
    print("Enter Obstacle coordinates in the form (x,y)\n" + "Enter -1 -1 to terminate")
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    ox.append(0)
    oy.append(0)
    ox.append(1000)
    oy.append(1000)
    while a!=-1 and b!=-1:
        ox.append(a)
        oy.append(b)
        s = input().split()
        a = int(s[0])
        b = int(s[1])
    return ox,oy
def path_planning(x_in, y_in, gx, gy, ox,oy):
    """
    gx: goal x position [m]
    gx: goal x position [m]
    ox: x position list of Obstacles [m]
    oy: y position list of Obstacles [m]
    reso: grid resolution [m]
    rr: robot radius[m]
    """
    reso = 1
    rr = 1
    print("Starting the process")
    ares_main=0
    rx=x_in
    ry=y_in
    while rx!=gx and ry!=gy:
        ares_main=ares_main+1
        rx, ry = a_star_planning(rx, ry, gx, gy, ox, oy, reso, rr)
        if rx==gx and ry==gy:
            break
        '''
        Suppose we also get feedback corresponding to the location of the rover as input
        then we can do incorporate that as wellself.

        if bool variable feed_loc is true then the revised location of rover will be used
        for path path_planning
        '''
        if 1:

            ox,oy = revise_obstacle_coordinates(ox,oy)
            print("Enter 1 for location feedback")
            feed_loc = int(input())
            if feed_loc is 1:
                print("Enter new coordinates")
                d = input().split()
                rx = int(d[0])
                ry = int(d[1])


    print("Yeah! We reached the target")









#main

print("Lets start working")
print("Enter starting position coordinates")
d = input().split()
x_in = int(d[0])
y_in = int(d[1])

print("Enter goal coordinates")
d = input().split()
gx = int(d[0])
gy = int(d[1])
ox=[0,1000]
oy=[0,1000]
ox, oy = revise_obstacle_coordinates(ox,oy)
path_planning(x_in, y_in, gx, gy, ox,oy )
