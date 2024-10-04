#include <iostream>

int main() {
    for (int i = 1; i <= 10; ++i) {
        if (i % 2 == 0) {
            std::cout << i << " is even" << std::endl;
        } else {
            std::cout << i << " is odd" << std::endl;
        }
    }
    return 0;
}