#include <string>
#include <vector>
#include <queue>

using namespace std;

int level_cnt[10]; // 문서의 중요도별 갯수를 저장한다.
queue<pair<int,int>> q; // first: 현재 문서의 중요도, second: 현재 문서의 처음 입력 받았을 때의 위치

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    //처음 입력 데이터 처리
    for(int i=0; i< priorities.size();i++){
        
        
        q.push({priorities[i],i}); // q.push({현재문서의 중요도,현재 문서의 처음 입력 받았을 때의 위치})
        level_cnt[priorities[i]]++;
    }
    
    int cnt = 1;
    
    while(!q.empty()){
        
        int selected_level; // 뽑을 문서의 중요도 숫자를 고를 변수
        
        for(int i = 9; i>= 1; i--){
            
            if(level_cnt[i] >= 1){
                level_cnt[i]--;
                selected_level = i;
                break;
            }
            
        }
        
        while(q.front().first != selected_level){
            pair<int,int> tmp = q.front();
            q.push(tmp);
            q.pop();
        }
        
        if(q.front().second == location){
            break;
        }
        
        q.pop();
        cnt++;
        
    }
    
    return cnt;
}