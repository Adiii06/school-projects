//The code is to to calculate and display the average of each group of numbers in the file created.
//Written by: Ma. Addine Anne T. Carreon
//Date: April 20, 2023
//Time: 3:10 PM
// Program: BSDS
//Course: CS127-5L
//Section: A35
//School: MAPUA University

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main() {
    std::ifstream infile("Data.txt");

    if (!infile) {
        cout << "Error opening file\n"; 
        return 1;
    }

    int num_items, num;
    double sum, avg;
    while (infile >> num_items) {
        sum = 0.0;
        cout << "The number of data in this group is " << num_items << "\n";
        
        cout << "The data in this group are: " ;
        for (int x = 1; x <= num_items; x++)
        {
            infile >> num;
            cout << num << " ";
            sum += num;
        }
        cout << endl;

        avg = sum / num_items;
        cout << "The average of the group of " << num_items << " numbers is " << std::fixed << std::setprecision(2) << avg << "\n";
        cout << endl;
    }

    infile.close();
    return 0;
}
