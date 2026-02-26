//The code is to take the length and width of the rectangle, then the results, including area and perimeter will be displayed
//Written by: Ma. Addine Anne T. Carreon
//Date: March 02, 2023
//Time: 10:54
//Course: CS127-5L
//Section: A35
//School: MAPUA University

#include <iostream>
#include <iomanip>

using namespace std;

//The function is to provide computation of the Rectangle
class Rectangle {
private:
	double length;
	double width;

public:

	void setData(double l, double w) {
		length = l;
		width = w;
	}

	double perimeter() {
		return 2 * (length + width);
	}

	double area() {
		return length * width;
	}

	void showData() {
		cout << "Lenght: " << length << endl;
		cout << "Width: " << width << endl;
		cout << "Perimeter: " << perimeter() << endl;
		cout << "Area: " << area() << endl;
	}
};

    //The function is to properly utilize the use of classes
	int main() {
		Rectangle r;
		double l, w;

		cout << "Enter the length: ";
		cin >> l;
		cout << "Enter the width: ";
		cin >> w;

		r.setData(l, w);
		cout << endl;
		r.showData(); 
		return 0;
	}