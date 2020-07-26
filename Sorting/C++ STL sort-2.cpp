//sort( )함수는 C++의 algorithm 헤더에 포함 
//데이터를 pair를 사용하여 처리(처리속도가 빨라서 코테에 적합)

#include <iostream>
#include <vector> 
#include <algorithm>

using namespace std;

//pair를 이용해서 3가지 정보를 묶을 수 있다 
bool compare(pair<string, pair<int, int> > a, pair<string, pair<int, int> > b) {
	if(a.second.first == b.second.first){				//성적 비교 후 같으면 
		return a.second.second>b.second.second;			//생년월일 비교 
	}
	else{
		return a.second.first > b.second.first;			//성적 다르면 낮은거 먼저 
	}
}

int main(void){
	vector<pair<string, pair<int, int> > >v;
	v.push_back(pair<string, pair<int, int> >("나동빈", make_pair(90, 19961222)));
	v.push_back(pair<string, pair<int, int> >("박한올", make_pair(95, 19930203)));
	v.push_back(pair<string, pair<int, int> >("이태일", make_pair(97, 19930518)));
	v.push_back(pair<string, pair<int, int> >("강종구", make_pair(88, 19900302)));
	v.push_back(pair<string, pair<int, int> >("이상욱", make_pair(90, 19921207)));
	
	sort(v.begin(), v.end(), compare);
	for(int i=0; i<v.size(); i++){
		cout<<v[i].first<<' ';
	}
	return 0;
}
