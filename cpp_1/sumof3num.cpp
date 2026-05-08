#include <iostream>
using namespace std;

int main() {
    int num1;
    int num2;
    int num3;

    cout << "Hi" << endl;
    cout << "Please input num1" << endl;
    cin >> num1;

    cout << "Please input num2" << endl;
    cin >> num2;

    cout << "Please input num3" << endl;
    cin >> num3;

    cout << "Calculating..." << endl;

    int total_num =  num1 + num2 + num3;

    cout << "Total sum of your number is " << total_num << endl;

    return 0;
}   