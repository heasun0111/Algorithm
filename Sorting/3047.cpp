//선택정렬
#include <stdio.h>

int x[3];
int num, index, temp;

int main(){
	
	int min;
	char string; 
		
	for(int i=0; i<3; i++){
		scanf("%d", &x[i]);
	}
	scanf("%s", &string);
	printf("%s", string);
	
	for(int i=0; i<3; i++){
		min=101;
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
	
	if(string=='ABC'){
		printf("%d %d %d", x[0], x[1], x[2]);
	}
	
	
	
}
