//선택정렬
#include <stdio.h>

int x[3];
int num, index, temp;

int main(){
	
	int min;
		
	for(int i=0; i<3; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<3; i++){
		min=1000001;
		for(int j=i; j<3; j++){
			if(min>x[j]){
				min=x[j];
				index=j;
			}
		}
		temp=x[i];
		x[i]=x[index];
		x[index]=temp;
		
	}
	
	for(int i=0; i<3; i++){
		printf("%d ", x[i]);
	}
	
	
}
