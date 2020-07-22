//»ğÀÔ Á¤·Ä
#include <stdio.h>

int x[3];
int temp;

 int main(){
 			
	for(int i=0; i<3; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<2; i++){	
		int j=i;						 
		while(x[j]>x[j+1] && j>=0){
			temp=x[j+1]; 
			x[j+1]=x[j];
			x[j]=temp;
			j--;
		}
	}
	
	for(int i=0; i<3; i++){
		printf("%d ",x[i]);
	}
	
}
