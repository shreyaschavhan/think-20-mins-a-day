//  Modify the program above to ask the user to enter floating-point values and store them in double variables. Compare the outputs of the two programs for some inputs of your choice. Are the results the same? Should they be? What’s the difference?

#include <bits/stdc++.h>
using namespace std;

int main(){
    double val1, val2;
    cout << "Enter two values: ";
    cin >> val1 >> val2;
    if (val1 > val2){
        cout << "Smaller: " << val2 << endl;
        cout << "Larger: " << val1 << endl;
    }
    else{
        cout << "Smaller: " << val1 << endl;
        cout << "Larger: " << val2 << endl;
    }
    cout << "Sum: " << val1 + val2 << endl;
    cout << "Difference: " << val1 - val2 << endl;
    cout << "Product: " << val1 * val2 << endl;
    cout << "Ratio: " << val1 / val2 << endl;
}