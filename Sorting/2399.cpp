#include <stdio.h>
#include <stdlib.h>
int x[10000];
int n=0;
long long sum;
long long ans=0;
	
int main(){
	
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		scanf("%d", &x[i]);
	}
	
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			sum=0;
			sum=x[j]-x[i];
			ans+=abs(sum);
			
		}
	}
	printf("%lli", ans);
	
	
	
}
