#include <stdio.h>

int N, K;
int x[1000];
int min, index, temp;

int main(){
	
	scanf("%d %d", &N, &K);	
	for(int i=0; i<N; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<N; i++){
		min=2147483646;
		for(int j=i; j<N; j++){
			if(min>x[j]){
				min=x[j];
				index=j;
			}
		}
		temp=x[i];
		x[i]=x[index];
		x[index]=temp;
		
	}
	
	printf("%d", x[K-1]);
	
	
}
