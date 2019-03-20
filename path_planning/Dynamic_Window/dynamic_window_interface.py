import numpy as np
import math
from matplotlib import pyplot as plot

from obstacle_coordinate_path_planning import Config
from obstacle_coordinate_path_planning import motion, calc_dynamic_window, calc_trajectory, calc_final_input, calc_obstacle_cost, calc_to_goal_cost, dwa_control, plot_arrow

def revise_obstacle_coordinates(obstac_coordinates):
    print("Enter Obstacle coordinates in the form (x,y)\n" + "Enter -1 -1 to terminate")
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    while a!=-1 and b!=-1:
        r = np.array([[a,b]])
        obstac_coordinates = np.concatenate((obstac_coordinates,r),axis=0)
        s = input().split()
        a = int(s[0])
        b = int(s[1])
        print(len(obstac_coordinates))
def path_planning(x_in, y_in, gx, gy, obstac_coordinates):

    '''


    x_in=x #currrent x position
    y_in=y #current y position


    print(x)
    print(y)


    # goal position
    gx=100
    gy=100

    '''

    # initial state [x(m), y(m), yaw(rad), v(m/s), omega(rad/s)]
    x = np.array([x_in, y_in, math.pi / 8.0, 0.0, 0.0])

    # goal position [x(m), y(m)]
    goal = np.array([gx, gy])
    # obstacles [x(m) y(m), ....]

    '''
    ob = np.array([[-1, -1],
                   [0, 2],
                   [40.0, 2.0],
                   [50.0, 4.0],
                   [50.0, 5.0],
                   [50.0, 6.0],
                   [50.0, 9.0],
                   [80.0, 9.0],
                   [70.0, 9.0],
                   [90.0, 9.0],
                   [110.0,11.0],
                   [120.0, 12.0]
                   ])
    '''

    u = np.array([0.0, 0.0])
    config = Config() #rover parameters
    traj = np.array(x)
    ob = obstac_coordinates


    for i in range(1000):
        revise_obstacle_coordinates(ob)
        u, ltraj = dwa_control(x, u, config, goal, ob)
        x = motion(x, u, config.dt)
        traj = np.vstack((traj, x))  # store state history


        print("u")
        print(u)
        print("ltraj")
        print(ltraj)


        '''


        if show_animation:
            plt.cla()
            plt.plot(ltraj[:, 0], ltraj[:, 1], "-g")
            plt.plot(x[0], x[1], "xr")
            plt.plot(goal[0], goal[1], "xb")
            plt.plot(ob[:, 0], ob[:, 1], "ok")
            plot_arrow(x[0], x[1], x[2])
            plt.axis("equal")
            plt.grid(True)
            plt.pause(0.0001)


        '''
        # check goal
        if math.sqrt((x[0] - goal[0])**2 + (x[1] - goal[1])**2) <= config.robot_radius:
            print("Goal!!")
            break

    print("Done")
    '''

    if show_animation:
        plt.plot(traj[:, 0], traj[:, 1], "-r")
        plt.pause(0.0001)
        plt.show()
    '''





print("Lets start working")
print("Enter starting position coordinates")
d = input().split()
x_in = int(d[0])
y_in = int(d[1])

print("Enter goal coordinates")
d = input().split()
gx = int(d[0])
gy = int(d[1])



obstac_coordinates = np.array([[10,10]])
revise_obstacle_coordinates(obstac_coordinates)
path_planning(x_in, y_in, gx, gy, obstac_coordinates )
