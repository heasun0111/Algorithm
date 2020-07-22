//삽입 정렬
#include <stdio.h>

int N=0;
int x[1000];
int temp;

 int main(){
 			
	scanf("%d", &N);
	for(int i=0; i<N; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<N-1; i++){
		int j=i;				// i부터 역순으로 숫자 비교 		 
		while(x[j]>x[j+1] && j>=0){
			temp=x[j+1];
			x[j+1]=x[j];
			x[j]=temp;
			j--;			// --부호로 역순으로 비교
		}
	}
	
	for(int i=0; i<N; i++){
		printf("%d\n",x[i]);
	}
	
}
