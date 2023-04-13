#include <bits/stdc++.h>
using namespace std;

int main(){
    int count = 0;
    string previous = "";
    string current;
    while (cin >> current){
        if (current == previous){
            count++;
        }
        previous = current;
    }
    cout << count;
}