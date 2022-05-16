#include <iostream>
#include <string>
#include <algorithm>
using namespace std;



int main(){


    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string str;

    cin >> str;

    // 주어진 문자열을 정렬해보면 정렬된 숫자가 나오고 그 이후에 정렬된 알파벳들이 나온다.

    sort(str.begin(),str.end());

    cout << "str: " << str << "\n";

    // 정답을 출력할 빈 문자열 배열
    string ans = "";

    for (int i = 0; i < str.size(); i++) {

        if (str[i] >= 'A' && str[i] <= 'Z') {
            ans += str[i];
        }

    }

    int num = 0;
    bool num_check = false;
    for (int i = 0; i < str.size(); i++) {

        if (str[i] >= '0' && str[i] <= '9') {
            num += str[i] - '0';
            num_check = true;
        }

    }

    if(num_check){
        ans = ans + to_string(num);
    }

    cout << ans;



    return 0;
}