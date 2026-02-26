//The code is to use structure for storing stock name, estimated earnings per share, and its estimated price-to-earning ratio
//Written by: Ma. Addine Anne T. Carreon
//Date: March 16, 2023
//Time: 2:20 PM
// Program: BSDS
//Course: CS127-5L
//Section: A35
//School: MAPUA University

#include <iostream>
#include <iomanip>

using namespace std;

struct Stock
{
    string StockName;
    double EstimatedEarningPShare;
    double EstimatedPriceTEarning;
};

int main()
{
    struct Stock TheStocks;
    for (int x = 0; x< 5; x++)
    {
        cout << "Enter the name of the stock: ";
        cin >> TheStocks.StockName;
        cout << "Enter the estimated earning per share: ";
        cin >> TheStocks.EstimatedEarningPShare;
        cout << "Enter the estimated price-to-earnings: ";
        cin >> TheStocks.EstimatedPriceTEarning;
        cout << "The anticipated stock price for the share of " << TheStocks.StockName << "'s Stock" << " is $" << fixed << setprecision(2) << TheStocks.EstimatedEarningPShare * TheStocks.EstimatedPriceTEarning << endl;
        cout << endl;
    }
    return 0;
}