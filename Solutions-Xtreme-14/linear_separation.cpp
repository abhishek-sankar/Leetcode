#include <bits/stdc++.h>

using namespace std;
    
void doStuff(){
	int n;
	int label_val;
	float x_val, y_val;
	cin>>n;
	map<pair<float, float>, int>labels;
	for(int i=0;i<n;i++){
		cin>>x_val>>y_val>>label_val;
		labels.insert({{x_val, y_val}, label_val});
	}
	for(auto i: labels){
		bool flag_1 = 0, flag_2 = 0;
		for(auto j: labels){
			if(i.first != j.first){
				
			}
		}
	}
}
int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		doStuff();
	}
	return 0;
}

//     //if such a line exists, it would be possible to rotate it 
//     //till it hits 2 points P and Q. Essentially, O(N^2) to select P and Q 
//     //and O(N) to check for each selection
//     //is there a better way?
//     //Hold up, choose one of the points as origin and you'll have it as O(N^2)
//     // checking if its on one side, could be either side
//     // 2 flags, each will be changed if its corresponding side gets a point
//     // if its all doable on one side, (0/1) or (1/0) works
//     // extended to all 4 cases, all -1s up/down and 1s up/down
//     //call me, if you didn't understand btw (Abhishek)
    
// void result() {
//     int T, label_val;
//     float x_val, y_val;
//     cin>>T;
//     map<pair<float, float>, int>labelled_points;
    
//     for(int i=0;i<T;i++){
//         cin>>x_val>>y_val>>label_val;
//         labelled_points.insert({{x_val, y_val}, label_val});
//     }
//     for(auto i: labelled_points){
//         int flag_1 = 0, flag_2 = 0;

//         for(auto j: labelled_points){
//             if(j.first!=i.first){
//                 if(j.second*((0-i.first.first)*(j.first.second - i.first.second) - (0-i.first.second)*(j.first.first - i.first.first))<0){
//                     //>=0 means it is right
//                     flag_1 = 1;
//                 }
//                 if(j.second*((0-i.first.first)*(j.first.second - i.first.second) - (0-i.first.second)*(j.first.first - i.first.first))>0){
//                     flag_2 = 1;
//                 }
//             }
//         }
//             if(flag_1 == 0 || flag_2 == 0){
//                 cout<<"YES"<<endl;
//                 return;
//             }        
//     }
//     //check flags and return appropriately
//     cout<<"NO"<<endl;
// }
// int main(){
//     int n;
//     cin>>n;
//     for(int i=0;i<n;i++){
//         result();
//     }
// }