//  Write a program that prompts the user to enter three integer values, and then outputs the values in numerical sequence separated by commas. So, if the user enters the values 10 4 6, the output should be 4, 6, 10. If two values are the same, they should just be ordered together. So, the input 4 5 4 should give 4, 4, 5.

#include <bits/stdc++.h>
using namespace std;

int main(){
    int num1, num2, num3;
    cout << "Enter three digits: ";
    cin >> num1 >> num2 >> num3;
    if (num1 <= num2 && num1 <= num3) {
       cout << num1 << ", ";
       if (num2 <= num3) {
           cout << num2 << ", " << num3 << endl;
       } else {
           cout << num3 << ", " << num2 << endl;
       }
   } else if (num2 <= num1 && num2 <= num3) {
       cout << num2 << ", ";
       if (num1 <= num3) {
           cout << num1 << ", " << num3 << endl;
       } else {
           cout << num3 << ", " << num1 << endl;
       }
   } else {
       cout << num3 << ", ";
       if (num1 <= num2) {
           cout << num1 << ", " << num2 << endl;
       } else {
           cout << num2 << ", " << num1 << endl;
       }
   }
}