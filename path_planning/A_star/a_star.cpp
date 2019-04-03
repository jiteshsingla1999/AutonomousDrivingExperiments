#include<bits/stdc++.h>
#include <tr1/unordered_map>
using namespace std::tr1;
using namespace std;
int motion[8][3];
    double minx,miny,maxx,maxy,xw,yw,xwidth,ywidth;
class coordinates
{
public:
  double x,y;
  coordinates(double x, double y)
  {
    this->x = x;
    this->y = y;
  }
};
class node
{
public:
  double x,y,cost;
  int p_index;


  node()
  {
	x=0;y=0;cost=0;

  }
  node(double x, double y, double cost, int p_index)
  {
    this->x = x;
    this->y = y;
    this->cost = cost;
    this->p_index=p_index;
  }

};
bool verify_node( node node1, int **obmap, int minx, int miny, int maxx, int maxy);
int find_min(int * obs, int n);
int find_max(int * obs, int n);
int ** calc_obstacle_map(int *obsx, int *obsy, int obsn, int reso, int rr);
void get_motion_model();
double calc_heuristic(node n1, node n2);


int calc_index(node n, double xwidth, double xmin, double ymin)
{
  return (n.y - ymin)*xwidth + (n.x-xmin);
}

coordinates a_star_planning(double sx, double sy, double gx, double gy, int * obsx, int * obsy, int obsn, int reso, int rr  )
{
  /*
    gx: goal x position [m]
    gx: goal x position [m]
    obsx: x position list of Obstacles [m]
    obsy: y position list of Obstacles [m]
    obsn: number of obstacles
    reso: grid resolution [m]
    rr: robot radius[m]
    */
    node nstart = node(sx/reso, sy/reso, 0.0, -1);
    node ngoal = node(gx/reso, gy/reso, 0.0, -1);

    for(int i=0;i<obsn;i++)
    {
      obsx[i] = obsx[i]/reso;
      obsy[i] = obsy[i]/reso;
    }

    int ** obmap = calc_obstacle_map(obsx, obsy, obsn, reso, rr);
    get_motion_model();

    typedef unordered_map <int, node> pppp;
    pppp openset;
    pppp closedset;
    ///unordered_map <int, node> closedset;
    openset[calc_index(nstart, xw, minx, miny)] = nstart;


    while(1)
    {
      double min_temp = INT_MAX;
      int cid=0;
      for(pppp:: const_iterator i = openset.begin(); i!=openset.end(); ++i)
      {
        double rr = (i->second).cost + calc_heuristic(ngoal, i->second);
        if(rr<min_temp)
        {
          min_temp=rr;
          cid = i->first;
        }

      }
      node current = openset[cid];
      cout << current.x << "," <<  current.y << endl;

      if ( current.x == ngoal.x && current.y == ngoal.y)
      {
              cout << "Find goal\n";
              ngoal.p_index = current.p_index;
              ngoal.cost = current.cost;
              break;
      }


      openset.erase(cid);
      closedset[cid] = current;

      for(int j=0;j<8;j++)
      {
        node dummy = node(current.x + motion[j][0],
                          current.y + motion[j][1],
                          current.cost + motion[j][2], cid);
        int n_id = calc_index(dummy, xw, minx, miny);

        if(closedset.find(n_id)!=closedset.end())
              continue;
        if(verify_node(dummy, obmap, minx, miny, maxx,maxy)==0)
          continue;
        if(openset.find(n_id)==openset.end())
        {
          openset[n_id] = dummy;
        }
        else
        {
          if(openset[n_id].cost>=dummy.cost)
          {
            openset[n_id] = dummy;
          }
        }

      }

    }


}

bool verify_node( node node1, int **obmap, int minx, int miny, int maxx, int maxy)
{
  if(node1.x<minx)
    return 0;
  else if(node1.y<miny)
    return 0;
  else if(node1.x>=maxx || node1.y>=maxy)
    return 0;

  if(obmap[int(node1.x)][int(node1.y)])
    return 0;


  return 1;
}



int find_min(int * obs, int n)
{
  int min = obs[0];
  for(int i=1;i<n;i++)
  {
    if(min>obs[i])
    min=obs[i];
  }
  return min;
}
int find_max(int * obs, int n)
{
  int min = obs[0];
  for(int i=1;i<n;i++)
  {
    if(min<obs[i])
    min=obs[i];
  }
  return min;
}
int ** calc_obstacle_map(int *obsx, int *obsy, int obsn, int reso, int rr)
{
  minx = find_min(obsx, obsn);
  miny = find_min(obsy, obsn);

  maxx = find_max(obsx, obsn);
  maxy = find_max(obsy, obsn);

  xwidth = maxx-minx;
  ywidth = maxy-miny;

  //size of map is 100 by 100
  int ** obmap = new int*[101];
  for(int i=0;i<101;i++)
  {
  obmap[i] = new int[101];
  for(int j=0;j<=100;j++)
  obmap[i][j]=0;
  }

  for(int j=0;j<obsn;j++)
  {
      obmap[int(obsx[j]-minx)][int(obsy[j]-miny)]=1;
  }

  return obmap;
}

void get_motion_model()
{
    // dx, dy, cost


    motion[0][0]=1;
    motion[0][1]=0;
    motion[0][2]=1;
    motion[1][0]=0;
    motion[1][1]=1;
    motion[1][2]=1;
    motion[2][0]=-1;
    motion[2][1]=0;
    motion[2][2]=1;
    motion[3][0]=0;
    motion[3][1]=-1;
    motion[3][2]=1;
    motion[4][0]=-1;
    motion[4][1]=-1;
    motion[4][2]=sqrt(2);
    motion[5][0]=-1;
    motion[5][1]=1;
    motion[5][2]=sqrt(2);
    motion[6][0]=1;
    motion[6][1]=-1;
    motion[6][2]=sqrt(2);
    motion[7][0]=1;
    motion[7][1]=1;
    motion[7][2]=sqrt(2);


}


double calc_heuristic(node n1, node n2)
{
    double w = 1.0;  //# weight of heuristic
    double d = w * sqrt((n1.x - n2.x)*(n1.x - n2.x) + (n1.y - n2.y)*(n1.y - n2.y));
    return d;
}
int main()
{
  cout << "Test1";
}
