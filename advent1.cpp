#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    // Create a text string, which is used to output the text file
    string line;
    int sum = 0;
    // Read from the text file
    ifstream file("puzzle1.txt");

    // Use a while loop together with the getline() function to read the file line by line
    while (getline (file, line)) { // iterate over every line in "puzzle1.txt"
        vector<char> digits;
        for(char& c : line) { // iterate over char in line
            if(isdigit(c)) {
                digits.push_back(c);
            }
        }
        int firstDigit = digits.front() - '0'; // convert char digit to int
        int secondDigit = digits.back() - '0'; // convert char digit to int
        int number = 10 * firstDigit + secondDigit;
        sum += number;
        cout << "Sum: "  << sum << " Number: " << secondDigit << endl;
    }

    // Close the file
    file.close();
}