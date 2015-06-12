#include <iostream>
using namespace std;

int main(int argv, char ** argc) {
	if ( argv >= 3 ) {
		cout << argc[1] << endl;
		cout << argc[2] << endl;
	}
}