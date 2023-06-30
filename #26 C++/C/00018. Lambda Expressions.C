#include <iostream>

int main() {
    int x = 5;
    int y = 10;

    auto sum = [](int a, int b) {
        return a + b;
    };

    int result = sum(x, y);
    std::cout << "Result: " << result << std::endl;

    return 0;
}