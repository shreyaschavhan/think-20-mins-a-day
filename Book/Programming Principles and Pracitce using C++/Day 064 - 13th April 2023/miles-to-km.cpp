//  Write a program in C++ that converts from miles to kilometers. Your program should have a reasonable prompt for the user to enter a number of miles. Hint: There are 1.609 kilometers to the mile.

#include <bits/stdc++.h>
using namespace std;

int main(){
    double miles;
    cout << "Enter miles: ";
    cin >> miles;
    cout << "Equivalent in KMs: " << miles * 1.609;
}