//��������
#include <stdio.h>

int N=0;
int x[1000];
int num, temp, index;

int main(){
	
	int min;
		
	scanf("%d", &N);
	for(int i=0; i<N; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<N; i++){
		min=9999;						//min�� ��ġ ���!! 
		for(int j=i; j<N; j++){			//j=i���� 
			if(min>x[j]){
				min=x[j];
				index=j;
			}
		}
		temp=x[i];
		x[i]=x[index];
		x[index]=temp;
		
	}
	
	for(int i=0; i<N; i++){
		printf("%d\n", x[i]);
	}
	
	return 0;	
	
}
