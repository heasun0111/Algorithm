//버블 정렬
#include<stdio.h>
 
int x[3];
int temp;

 int main(){
 			
	for(int i=0; i<3; i++){
		scanf("%d", &x[i]);
	}
	for(int i=0; i<3; i++){
		for(int j=0; j<3-i-1; j++ ){		//j<N-i-1 주의!! 
			if(x[j]>x[j+1]){
				temp=x[j+1];
				x[j+1]=x[j];
				x[j]=temp;
			}
		}
	}
	
	for(int i=0; i<3; i++){
		printf("%d ", x[i]);
	}
 	
 } 
