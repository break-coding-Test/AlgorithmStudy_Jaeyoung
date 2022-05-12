#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool cmp(int num1, int num2){
    
    string str1 = to_string(num1);
    string str2 = to_string(num2);
    
    // 숫자를 앞 뒤로 순서를 바꾼 것 중에서 큰 수를 앞으로 정렬
    return str1 + str2 > str2 + str1;
    

    
}

string solution(vector<int> numbers) {
    string answer = "";
    

    
    sort(numbers.begin(), numbers.end(),cmp);
    
    for(int i=0; i<numbers.size(); i++){
        answer += to_string(numbers[i]);
    }
    
    if(answer[0] == '0'){
        return "0";
    }
    
    return answer;
}