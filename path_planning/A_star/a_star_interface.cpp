#include<bits/stdc++.h>
#include "a_star.cpp"
#define pb push_back
using namespace std;


void revise_obstacle_coordinates(vector<int>  &ox, vector<int>  &oy)
{
    printf("Enter Obstacle coordinates in the form (x,y)\nEnter -1 -1 to terminate");
    double a,b;
    cin >> a >> b;
    ox.pb(0);
    oy.pb(0);
    ox.pb(1000);
    oy.pb(1000);
    while (a!=-1 && b!=-1)
    {
        ox.pb(a);
        oy.pb(b);
        cin >> a >> b;

      }

    return ;
}



void path_planning(double x_in, double y_in, double gx, double  gy, vector<int> ox, vector<int> oy){
    /*
    gx: goal x position [m]
    gx: goal x position [m]
    ox: x position list of Obstacles [m]
    oy: y position list of Obstacles [m]
    reso: grid resolution [m]
    rr: robot radius[m]
    */
    int reso = 1;
    int rr = 1;
    printf("Starting the process");
    int ares_main=0;
    double rx=x_in;
    double ry=y_in;
    while (rx!=gx and ry!=gy)
    {
        ares_main=ares_main+1;
        coordinates ggkk(67,7);

        ggkk = a_star_planning(rx, ry, gx, gy, ox, oy, ox.size(), reso, rr);
        rx = ggkk.x;
        ry = ggkk.y;
        if (rx==gx and ry==gy)
            break;
      /*
        Suppose we also get feedback corresponding to the location of the rover as input
        then we can do incorporate that as wellself.

        if bool variable feed_loc is true then the revised location of rover will be used
        for path path_planning
        */


            revise_obstacle_coordinates(ox,oy);
            printf("Enter 1 for location feedback\n");
            int feed_loc;
            cin >> feed_loc;
            if (feed_loc == 1)
            {
                printf("Enter new coordinates\n");
                cin >> rx >> ry;
              }

      }


    printf("Yeah! We reached the target");

}

int main()
{

printf("Lets start working\n");
printf("Enter starting position coordinates");


double x_in, y_in,gx,gy;
cin >> x_in >> y_in;

printf("Enter goal coordinates");
cin >> gx >> gy;
vector<int> ox;
vector<int>oy;
revise_obstacle_coordinates(ox,oy);

path_planning(x_in, y_in, gx, gy, ox,oy );

}
