//sort( )함수는 C++의 algorithm 헤더에 포함 
//데이터를 class로 묶어서 정렬(실무에 적합)

#include <iostream>
#include <algorithm>

using namespace std;

class Student{
public:
	string name;
	int score;
	Student(string name, int score){
		this->name = name;
		this->score = score;	//생성자는 특정한 객체를 초기화하기 위해 사용 
	}
	bool operator <(Student &student){			//정렬 기준 
		return this->score < student.score;
	}
}; 

bool compare(int a, int b){
	return a > b;
}
int main(void){
	Student students[] = {
		Student("나동빈", 90),
		Student("이상욱", 93),
		Student("박한울", 97),
		Student("강종구", 87),
		Student("이태일", 92) 
	};
	sort(students, students + 5); 
	for(int i=0; i<5; i++){
		cout<<students[i].name<<' ';
	}
}
