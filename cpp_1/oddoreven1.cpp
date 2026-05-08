#include <iostream>

using namespace std;

int main(){
    int number;

    cout << "Input number" << endl;
    cin >> number;

    if (number % 2 == 0) {
        cout << "Is even" << endl;
    } 

    else {
        cout << "Is odd" << endl;
    }

    return 0;
}