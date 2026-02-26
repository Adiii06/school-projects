//The code is to enter a string using getline and read in reverse order
//Written by: Ma. Addine Anne T. Carreon
//Date: April 13, 2023
//Time: 3:15 PM
//Program: BSDS
//Course: CS127-5L
//Section: A35
//School: MAPUA University

#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;

    cout << "Enter a string: ";
    getline(cin, str);

    cout << "Reverse string: ";
    for (int x = str.length() - 1; x >= 0; x--) {
        cout << str.at(x);
    }

    return 0;
}


