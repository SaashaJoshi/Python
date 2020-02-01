#include<iostream>
#include<stack>
using namespace std;
#define NODE 7

typedef struct node
{
    int value;
    int state;
} node;

int graph[NODE][NODE] =
{
    {0, 1, 0, 0, 0, 0,0},
    {1, 0, 1, 1, 0, 0,0},
    {0, 1, 0, 0, 1, 0,0},
    {0, 1, 0, 0, 1, 1,0},
    {0, 0, 1, 1, 0, 0,1},
    {0, 0, 0, 1, 0, 0,1},
    {0,0,0,0,1,1,0}
};

void dfs(node *vertex, node start)
{
    node u;
    stack<node> s;

    for(int i = 0; i<NODE; i++)
    {
        vertex[i].state = 0;
    }

    s.push(start);

    while(!s.empty())
    {

        u = s.top();

        s.pop();
        cout << char(u.value+'A') << " ";

        if(u.state != 1)
        {

            u.state = 1;
            vertex[u.value].state = 1;

            for(int i = 0; i<NODE; i++)
            {
                if(graph[i][u.value])
                {
                    if(vertex[i].state == 0)
                    {

                        s.push(vertex[i]);
                        vertex[i].state = 1;

                    }
                }
            }
        }
        u.state=2;
    }
}

int main()
{
    node vertices[NODE];
    node start,dest;
    char s,d;

    for(int i = 0; i<NODE; i++)
    {
        vertices[i].value = i;
    }


    s = 'A';
    d = 'G';
    start.value = s-'A';
    dest.value = d -'A';
    //cout<<start.val<<endl;
//cout<<"start"<<endl;
    cout << "DFS Traversal: ";
    dfs(vertices, start);
    cout << endl;
}
