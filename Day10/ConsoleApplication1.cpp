
#include "stdafx.h"
#include <stdlib.h>
#include<iostream>
#include <math.h>
#include <fstream>
#include <sstream>
#include <string>
#define lengthOfLine 256

using namespace std;

int main()
{    
	string allLines;
	string line;
	ifstream myfile("C:/Users/Carlos/Documents/GitHub/Advent_of_code/Day10/input.txt");
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{
			allLines = allLines + line;
		}
		myfile.close();
	}
	cout << allLines << '\n';

	int arr[lengthOfLine] = {0};
	int auxArr[lengthOfLine] = {0};

	for (int i = 0; i < lengthOfLine; i++) {
		arr[i] = i;
	}

	// Split in python is string.split(",")
	string delimiter = ",";
	size_t pos = 0;
	std::string token;
	int index = 0;
	int skipSize = 0;
	

	while ((pos = allLines.find(delimiter)) != std::string::npos) {
		
		token = allLines.substr(0, pos);
		istringstream buffer(token);
		int value;
		buffer >> value;

		string show = to_string(index);
		cout << show << "\n --- \n";

		show = to_string(skipSize);
		cout << show << "\n --- \n";

		for (int j = 0; j < value; j++) {
			auxArr[j] = arr[(index + j) % lengthOfLine];
		}		

		int k = 0;
		for (int j = (value-1); j >= 0; j--) {			
			arr[(index + k) % lengthOfLine] = auxArr[j];
			k = k + 1;
		}
		
		index = (index + value + skipSize) % lengthOfLine;
		skipSize = skipSize + 1;
		

		for (int i = 0; i < lengthOfLine; i++) {
			string show = to_string(arr[i]) ;
			cout << show << "\n";
		}		

		cout << "\n -- \n";
		allLines.erase(0, pos + delimiter.length());
	}
	cout << "The result is: " << to_string(arr[0] * arr[1]);


	return 0;
}

