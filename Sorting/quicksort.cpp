/*
퀵 정렬(분할 정렬)
기준값을 기준으로 앞에는 작은 원소, 뒤에는 큰 원소가 오게 만들고
정렬이 이루어지면 또 다른 기준값으로 정렬을 한다.
*/
#include <stdio.h>

int number = 10;
int data[] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

void show() {
	int i;
	for (i = 0; i < number; i++) {
		printf("%d ", data[i]);
	}
}

void quickSort(int* data, int start, int end) {
	if (start >= end) {
		return;
	}

	int key = start;
	int i = start + 1;
	int j = end;
	int temp;

	while (i <= j) { // 엇갈리 때까지 반복
		while (i <= end && data[i] <= data[key]) {//왼쪽에서부터 key값보다 큰 값 찾는다
			i++;
		}
		while (j > start && data[j] >= data[key]) {//오른쪽에서부터 key값보다 작은 값 찾는다
			j--;
		}
		if (i > j) { //엇갈리면 키 값과 교체
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}
		else { //엇갈리지 않으면 i와 j교체
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
		}
		quickSort(data, start, j - 1);
		quickSort(data, j + 1, end);
	}
}

	int main(void) {
		quickSort(data, 0, number - 1);
		show();
		return 0;
	}
