
#include<iostream>
#include<queue>
#define NODE 6
using namespace std;

typedef struct node {
   int value;
   int state;
}node;

int graph[NODE][NODE] =
{
   {0, 1, 1, 1, 0, 0},
   {1, 0, 0, 1, 1, 0},
   {1, 0, 0, 1, 0, 1},
   {1, 1, 1, 0, 1, 1},
   {0, 1, 0, 1, 0, 1},
   {0, 0, 1, 1, 1, 0}
};

void bfs(node *vert, node s) {
   node u;
   int i, j;
   queue<node> q;

   for(i = 0; i<NODE; i++) {
      vert[i].state = 0;
   }

   vert[s.value].state = 1;
   q.push(s);

   while(!q.empty()) {
      u = q.front();
      q.pop();
      cout << char(u.value+'A') << " ";

      for(i = 0; i<NODE; i++) {
         if(graph[i][u.value])
          {

            if(vert[i].state == 0)
            {
               vert[i].state = 1;
               q.push(vert[i]);
            }
         }
      }
      u.state = 2;
   }
}

int main() {
   node vertices[NODE];
   node start;
   char s;

   for(int i = 0; i<NODE; i++) {
      vertices[i].value  = i;
   }

   s = 'B';
   start.value = s-'A';
   cout << "BFS Traversal: ";
   bfs(vertices, start);
   cout << endl;
}
