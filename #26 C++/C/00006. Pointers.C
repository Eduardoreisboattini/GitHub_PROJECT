#include <iostream>

int main() {
    int value = 42;
    int* pointer = &value;

    std::cout << "Value: " << value << std::endl;
    std::cout << "Pointer: " << pointer << std::endl;
    std::cout << "Dereferenced Pointer: " << *pointer << std::endl;

    return 0;
}