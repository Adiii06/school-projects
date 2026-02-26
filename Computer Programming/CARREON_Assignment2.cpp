#include <iostream>

using namespace std;

int main() {
	int pos = 0, nega = 0, zero = 0, x, arr[10];

	for (x = 0; x < 10; x++) {
		cout << "Type in number " << x + 1 << ": ";
		cin >> arr[x];
	}

	for (x = 0; x < 10; x++){
		if (arr[x] > 0)
			pos++;
		else if (arr[x] == 0)
			zero++;
		else
			nega++;
	}

	cout << "\nThe Number of Positive Integer/s is: " << pos;
	cout << "\nThe Number of Zero/s is: " << zero;
	cout << "\nThe Number of Negative Integer/s: " << nega;

	return 0;
}