// Author: Ma. Addine Anne T. Carreon
// Date: 04-27-2023
// Description: This program allows the user to select from a menu of options and perform different processes based on their selection.

#include <iostream>
#include <string>

using namespace std;

// Class definition for Employee
class maatcEmployee {
private:
    int maatcID; // employee ID number
    double maatcPayRate; // employee pay rate
    int maatcMaxHours; // maximum number of hours employee should work per week
public:
    // Constructor
    maatcEmployee() {
        maatcID = 0;
        maatcPayRate = 0.0;
        maatcMaxHours = 0;
    }

    // Setter functions
    void setID(int id) {
        maatcID = id;
    }

    void setPayRate(double rate) {
        maatcPayRate = rate;
    }

    void setMaxHours(int hours) {
        maatcMaxHours = hours;
    }

    // Getter functions
    int getID() const {
        return maatcID;
    }

    double getPayRate() const {
        return maatcPayRate;
    }

    int getMaxHours() const {
        return maatcMaxHours;
    }

    // Function to enter data for a new employee
    void enterData() {
        cout << "Enter employee ID: ";
        cin >> maatcID;
        cout << "Enter employee pay rate: ";
        cin >> maatcPayRate;
        cout << "Enter maximum hours employee should work per week: ";
        cin >> maatcMaxHours;
    }

    // Function to display existing data for an employee
    void displayData() const {
        cout << endl;
        cout << "Employee ID: " << maatcID << endl;
        cout << "Employee pay rate: " << maatcPayRate << endl;
        cout << "Maximum hours employee should work per week: " << maatcMaxHours << endl;
    }

};

// Function to display information about the program
void maatcAbout() {
    // Display information about the program and the author
    cout << "Author: Ma. Addine Anne T. Carreon" << endl;
    cout << "Student number: 2022108622" << endl;
    cout << "Date: 04-27-2023" << endl;
}

int main() {
    int choice;
    maatcEmployee employee;

    // Loop until user chooses to exit
    do {
        // Display menu
        cout << "Menu:" << endl;
        cout << "1. About" << endl;
        cout << "2. Employee" << endl;
        cout << "3. Exit" << endl;

        // Ask for user input
        cout << "Enter your choice: ";
        cin >> choice;
        cout << endl;

        // Process user input
        switch (choice) {
        case 1:
            maatcAbout();
            break;
        case 2:
            employee.enterData();
            employee.displayData();
            break;
        case 3:
            cout << "Exiting program." << endl;
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }

        // Re-display the menu after each process
        cout << endl;
    } while (choice != 3);

    return 0;
}
