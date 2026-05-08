#include <iostream>
using namespace std;

int x_cof;
int x_pwr;

void power_rule() {
    int new_cof = x_cof * x_pwr;
    int new_power = x_pwr - 1;
    cout << "Your derivative is " << new_cof << "x" << "^" << new_power << endl;
    }

int main() {

    cout << "Input coefficient of x" << endl;
    cin >> x_cof;
    cout << "Input coefficient of x power" << endl;
    cin >> x_pwr;

    if (x_pwr == 1) {
        cout << x_cof << endl;
        return 0;
    }

    else if (x_pwr == 0) {
        cout << "0" << endl;
        return 0;
    }

    else {
        power_rule();
    }

    return 0;
}