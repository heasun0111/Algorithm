//선택정렬
 
#include<stdio.h>

int x[4];
int num, index, temp;

int main(){
	
	for(int i=0; i<4; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<4; i++){
	int min=101;
	for(int j=i; j<4; j++){
		if(min>x[j]){
			min=x[j];
			index=j;
		}
	}
	temp=x[i];
	x[i]=x[index];
	x[index]=temp;		
	}
	
	int ans=x[0]*x[2];
	printf("%d", ans);
}
