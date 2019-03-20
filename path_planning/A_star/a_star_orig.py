
import matplotlib.pyplot as plt
import math

show_animation = False
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


class Node:

    def __init__(self, x, y, cost, pind):
        self.x = x
        self.y = y
        self.cost = cost
        self.pind = pind

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.cost) + "," + str(self.pind)





def a_star_planning(sx, sy, gx, gy, ox, oy, reso, rr):
    """
    gx: goal x position [m]
    gx: goal x position [m]
    ox: x position list of Obstacles [m]
    oy: y position list of Obstacles [m]
    reso: grid resolution [m]
    rr: robot radius[m]
    """



    nstart = Node(round(sx / reso), round(sy / reso), 0.0, -1)
    ngoal = Node(round(gx / reso), round(gy / reso), 0.0, -1)
    #ox = [iox / reso for iox in ox]
    #oy = [ioy / reso for ioy in oy]

    obmap, minx, miny, maxx, maxy, xw, yw = calc_obstacle_map(ox, oy, reso, rr)

    motion = get_motion_model()

    openset, closedset = dict(), dict()
    openset[calc_index(nstart, xw, minx, miny)] = nstart


    ares=0

    while 1:
        ares = ares+1

        if(ares%100==0):
            return current.x, current.y



        #print(len(openset))
        c_id = min(
        openset, key=lambda o: openset[o].cost + calc_heuristic(ngoal, openset[o]))
        current = openset[c_id]
        print(str(current.x) + "," + str(current.y) )



        if current.x == ngoal.x and current.y == ngoal.y:
            print("Find goal")
            ngoal.pind = current.pind
            ngoal.cost = current.cost
            break

        # Remove the item from the open set
        del openset[c_id]
        # Add it to the closed set
        closedset[c_id] = current

        # expand search grid based on motion model
        for i, _ in enumerate(motion):
            node = Node(current.x + motion[i][0],
                        current.y + motion[i][1],
                        current.cost + motion[i][2], c_id)
            n_id = calc_index(node, xw, minx, miny)
            #print("Node checking")


            if n_id in closedset:
                #print("Node already traversed")
                continue

            if not verify_node(node, obmap, minx, miny, maxx, maxy):
                #print("Invalid Node")
                continue

            #print("Node Passed")

            if n_id not in openset:
                openset[n_id] = node  # Discover a new node
            else:
                if openset[n_id].cost >= node.cost:
                    # This path is the best until now. record it!
                    openset[n_id] = node


    return gx,gy









def calc_heuristic(n1, n2):
    w = 1.0  # weight of heuristic
    d = w * math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)
    return d


def verify_node(node, obmap, minx, miny, maxx, maxy):

    if node.x < minx:
        return False
    elif node.y < miny:
        return False
    elif node.x >= maxx:
        return False
    elif node.y >= maxy:
        return False

    if obmap[node.x][node.y]:
        return False

    return True


def calc_obstacle_map(ox, oy, reso, vr):

    minx = round(min(ox))
    miny = round(min(oy))
    maxx = round(max(ox))
    maxy = round(max(oy))
    #print("minx:", minx)
    #print("miny:", miny)
    #print("maxx:", maxx)
    #print("maxy:", maxy)

    xwidth = round(maxx - minx)
    ywidth = round(maxy - miny)
    #print("xwidth:", xwidth)
    #print("ywidth:", ywidth)

    # obstacle map generation
    obmap = [[False for i in range(1100)] for i in range(1100)]
    for i in range(len(ox)):
        temp1 = int(ox[i])
        temp2 = int(oy[i])
        #print(str(temp1) + "," + str(temp2))
        obmap[temp1][temp2]=True
        #obmap[int(ox[i])][int(oy[i])]=True

    return obmap, minx, miny, maxx, maxy, xwidth, ywidth


def calc_index(node, xwidth, xmin, ymin):
    return (node.y - ymin) * xwidth + (node.x - xmin)


def get_motion_model():
    # dx, dy, cost
    motion = [[1, 0, 1],
              [0, 1, 1],
              [-1, 0, 1],
              [0, -1, 1],
              [-1, -1, math.sqrt(2)],
              [-1, 1, math.sqrt(2)],
              [1, -1, math.sqrt(2)],
              [1, 1, math.sqrt(2)]]

    return motion
