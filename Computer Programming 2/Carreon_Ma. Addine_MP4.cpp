//The code is to declare three one-dimensional arrays name miles, gallons and mpg.
//Written by: Ma. Addine Anne T. Carreon
//Date: March 30, 2023
//Time: 2:20 PM
// Program: BSDS
//Course: CS127-5L
//Section: A35
//School: MAPUA University

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double miles[10] = { 240.5, 300.0, 189.6, 310.6, 280.7, 216.9, 199.4, 160.3, 177.4, 192.3 };
    double gallons[10] = { 10.3, 15.6, 8.7, 1.4, 16.3, 15.7, 14.9, 10.7, 8.3, 8.4 };
    double mpg[10];
    double* a_mpg = mpg;

    for (int x = 0; x < 10; x++) {
        *(a_mpg + x) = miles[x] / gallons[x];
    }

    cout << "Miles \t\t Gallons \t MPG" << endl;
    for (int x = 0; x < 10; x++) {
        cout << fixed << setprecision(2) << miles[x] << "\t\t" << gallons[x] << "\t\t" << *(a_mpg + x) << endl;
    }
    return 0;
}
