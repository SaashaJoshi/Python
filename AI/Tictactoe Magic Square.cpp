#include<iostream>
using namespace std;
	int board[9];
	int turn = 1;
	int m[9]={8,3,4,1,5,9,6,7,2};

void user_move(){
	int move;
	cout << "Enter Your Move\n";
	cin >> move;
	if((move > 9) || (move < 1) || (board[move - 1] != 2)){
		cout << "INVALID...ENTER AGAIN\n";
		user_move();
	}
	else{
		board[move - 1] = 3;
		turn = turn + 1;
	}
}




int posswin(int a){

int k=0,c[9];
if(a==3)
{
for(int i=0;i<9;i++)
{
if(board[i]==3)
{
c[k]=i;
k++;
}
}
for(int i=0;i<k;i++)
for(int j=i+1;j<k;j++)
{
int temp=15-(m[c[i]]+m[c[j]]);
if(temp<=9&&temp>0)
{
for(int z=0;z<9;z++)
{
if(m[z]==temp)
if(board[z]==2)
return z;
}
}
}
return -1;
}
else if(a==5)
{
for(int i=0;i<9;i++)
{
if(board[i]==5)
{
c[k]=i;
k++;
}
}
for(int i=0;i<k;i++)
for(int j=i+1;j<k;j++)
{
int temp;
temp=15-(m[c[i]]+m[c[j]]);
if(temp<=9&&temp>0)
{
for(int z=0;z<9;z++)
{
if(m[z]==temp)
if(board[z]==2)
return z;
}
}
}
return -1;
}
}



void make2(){
	if(board[3]==2)
	{
	board[4]=5;

    }
	else if(board[0]==2)
	{
		board[0]=5;
	}
	else
	{
	if(board[5]==2)
	{
		board[5]=5;
	}
	else if(board[2] == 2)
	{
	    board[2] = 5;
    }
    else if(board[1]==2)
    {
    	board[1]=5;
	}
	else if(board[7] == 2)
	{
	board[7] = 5;
    }
    }
	
	
	if(board[3] == 2)
	board[3] = 5;
	
}





void comp_move(){
	int x;
switch(turn){

{
	board[0] = 5;
	turn = turn + 1;
	break;
}
case 2:
{
	if(board[4] == 2){
		board[4] = 5;
	}
	else
	board[0] = 5;
	turn = turn + 1;
	break;
}
case 3:
	{
	
	if(board[8] == 2){
		board[8] = 5;
	}
	else
	board[2] = 5;
	turn = turn + 1;
	break;
}
case 4:
	{
		if(board[4]==2){
			board[4]==5;
		}
		else if(board[0]==2)
		{
			board[0]==5;
		}
		
		x = posswin(3);
		if(x != -1)
		board[x] = 5;
		else{
			make2();
		}
		turn = turn + 1;
		break;
	}
case 5:
	{
		x = posswin(5);
		if(x != -1){
		board[x] = 5;
		}
		else {
			x = posswin(3);
			if(x != -1)
			board[x] = 5;
			else {
				
				if(board[6] == 2)
				board[6] = 5;
				else 
				board[2] = 5;
			}
		}
	turn = turn + 1;
	break;
	}
case 6:{
		x = posswin(5);
		if(x != -1)
		board[x] = 5;
		else {
			x = posswin(3);
			if(x != -1)
			board[x] = 5;
			else {
				make2();
			}
		}
	turn = turn + 1;
	break;
}
case 7:{
	x = posswin(5);
		if(x != -1)
		board[x] = 5;
		else {
			x = posswin(3);
			if(x != -1)
			board[x] = 5;
			else {
			make2();
			}
			}
	turn = turn + 1;
	break;
	
}
case 8:{
	x = posswin(5);
		if(x != -1)
		board[x] = 5;
		else {
			x = posswin(3);
			if(x != -1)
			board[x] = 5;
			else {
			make2();
			}
			}
	turn = turn + 1;
	break;
}
case 9:{
	x = posswin(5);
		if(x != -1)
		board[x] = 5;
		else {
			x = posswin(3);
			if(x != -1)
			board[x] = 5;
			else {
		    make2();
			}
			}
		turn = turn + 1;
	break;
}

}
}
void display(){
for (int i = 0; i <= 2; i++){
	if(board[i] == 2){
		cout << "__" << "\t";
	}
	if(board[i] == 3){
		cout << "x" << "\t";
	}
	if(board[i] == 5){
		cout << "0" << "\t";
	}
}
cout << "\n";
for (int i = 3; i <= 5; i++){
	if(board[i] == 2){
		cout << "__" << "\t";
	}
	if(board[i] == 3){
		cout << "x" << "\t";
	}
	if(board[i] == 5){
		cout << "0" << "\t";
	}
}
cout << "\n";
for (int i = 6; i <= 8; i++){
	if(board[i] == 2){
		cout << "__" << "\t";
	}
	if(board[i] == 3){
		cout << "x" << "\t";
	}
	if(board[i] == 5){
		cout << "0" << "\t";
	}
}
cout << "\n" << "\n" <<"\n";

}
void check_winner(){
if((board[0] * board[1] * board[2])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[3] * board[4] * board[5])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[6] * board[7] * board[8])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[0] * board[3] * board[6])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[1] * board[4] * board[7])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[2] * board[5] * board[8])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[0] * board[4] * board[8])	== 27){
	cout << "user wins";
	exit(0);
}
if((board[2] * board[4] * board[6])	== 27){
	cout << "user wins";
	exit(0);
}


if((board[0] * board[1] * board[2])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
if((board[3] * board[4] * board[5])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
if((board[6] * board[7] * board[8])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
if((board[0] * board[3] * board[6])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
if((board[1] * board[4] * board[7])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
if((board[2] * board[5] * board[8])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
if((board[0] * board[4] * board[8])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
    exit(0);
}
if((board[2] * board[4] * board[6])	== 125){
	cout<< "********\n";
	cout << "PC WINS\n";
	cout<< "********\n";
	exit(0);
}
}


void human_first(){
	user_move();
	display(); 
	check_winner(); 
	comp_move();
	display();
	check_winner();
}
void comp_first(){ 
	comp_move();
	display();
	check_winner();
	user_move();
	display();
	check_winner();
} 


int main()
{
		for(int i = 0;i <= 8; i++)
		{  
		board[i] = 2;
	    }
		char first;
	cout<< "***************************\n";	
	cout<< "TO PLAY FIRST **PRESS** ^Y^ \nTO PLAY SECOND **PRESS** ^N^ \n";
	cout<< "***************************\n";
	cin >> first;
	if(first == 'y')
	{
		while(turn <= 9)
		{
		human_first();
	    }
	}
	else {
	if(first == 'n'){
		while(turn <= 9){
		comp_first();
	}}
	else{
	cout << "INVALID INPUT\n";
	main();
    }
	}
	return 0;
}

