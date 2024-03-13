#include <iostream>

using namespace std;

int main() {
    int n;

    cout << "숫자를 입력: ";
    cin >> n;

    if (n == 1) {
        for (int i = 1; i <= 5; ++i) {
            for (int j = 1; j <= i; ++j) {
                cout << "*";
            }
            cout << endl;
        }
    } else if (n == 2) {
        for (int b = 5; b >= 1; --b) {
            for (int t = 1; t <= b; ++t) {
                cout << "*";
            }
            cout << endl;
        }
    } else if (n == 3) {
    	for (int a = 1; a<= 5; --a) {
    		for (int aa= 1; aa <= aa; --aa) {
                cout << "*";
			}
			cout << endl;
		}
	}

    return 0;
}

