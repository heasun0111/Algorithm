//버블 정렬
#include<stdio.h>
 
int N=0;
int x[1000];
int temp;

 int main(){
 			
	scanf("%d", &N);
	for(int i=0; i<N; i++){
		scanf("%d", &x[i]);
	}
	for(int i=0; i<N; i++){
		for(int j=0; j<N-i-1; j++ ){		//j<N-i-1 주의!! 
			if(x[j]>x[j+1]){
				temp=x[j+1];
				x[j+1]=x[j];
				x[j]=temp;
			}
		}
	}
	
	for(int i=0; i<N; i++){
		printf("%d\n", x[i]);
	}
 	
 } 
