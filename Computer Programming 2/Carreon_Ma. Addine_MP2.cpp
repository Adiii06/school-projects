//The code is to take the list of food, it can add, modify and delete items in the list
//Written by: Ma. Addine Anne T. Carreon
//Date: March 02, 2023
//Time: 11:50 
//Course: CS127-5L
//Section: A35
//School: MAPUA University

#include <iostream>
#include <iomanip>

using namespace std;

class Food
{
private:
    string type;
    string food;
public:
    Food(string = "basic", string = "Dairy"); // default constructor
    void displayValues(); // accessor
    // mutators
    void setType(string);
    void setFood(string);
};

Food::Food(string type, string name)
{
    this->type = type;
    this->food = food;
}

void Food::displayValues()
{
    cout << "Type: " << this->type << endl;
    cout << "Food: " << this->food << endl;
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
}

void Food::setType(string type)
{
    this->type = type;
}

void Food::setFood(string name)
{
    this->food = name;
}

int main()
{
    Food newFood1;
    string type, food;

    cout << "Food type option (Basic or Prepared): ";
    cout << endl;

    cout << "Basic food option:" << endl;
    cout << "[1] Dairy" << endl;
    cout << "[2] Meat" << endl;
    cout << "[3] Fruit" << endl;
    cout << "[4] Vegetable" << endl;
    cout << "[5] Grain" << endl;
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    cout << endl;

    cout << "1 Add a food item." << endl;
    cout << "2 Modify a food item." << endl;
    cout << "3 Delete a food item." << endl;
    cout << "4 Exit this menu." << endl;
    cout << "Option: ";

    int choice;
    cin >> choice;
    while (choice != 4)
    {
        switch (choice)
        {
        case 1: // add food
            cout << endl;
            cout << "Enter food type: ";
            cin >> type;
            cout << "Enter basic food item: ";
            cin >> food;
            newFood1.setFood(food);
            newFood1.setType(type);

            cout << endl;
            cout << "Added Food." << endl;
            newFood1.displayValues();
            break;
            cout << endl;

        case 2: // modify food data 
        {
            int choice;
            cout << "Enter 1 to change the type of food." << endl;
            cout << "Enter 2 to change basic food item." << endl;
            cout << "Option: ";
            cin >> choice;
            cout << endl;
            cout << "Enter new value: ";
            string newValue;
            cin >> newValue;
            if (choice == 1)
                newFood1.setType(newValue);
            else if (choice == 2)
                newFood1.setFood(newValue);
            cout << "Modified Food Data." << endl;
            newFood1.displayValues();
            break;
            cout << endl;
        }

        case 3: // delete Food
            newFood1.setType("");
            newFood1.setFood("");
            cout << "Deleted Food." << endl;
            break;
        }

        cout << endl;
        cout << "1 Add a food item." << endl;
        cout << "2 Modify a food item." << endl;
        cout << "3 Delete a food item." << endl;
        cout << "4 Exit this menu." << endl;
        cout << "Option: ";
        cin >> choice;
        cout << endl;
    }
    return 0;
}