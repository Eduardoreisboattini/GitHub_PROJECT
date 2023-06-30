#include <iostream>
#include <memory>

class MyClass {
public:
    void print() {
        std::cout << "Hello from MyClass!" << std::endl;
    }
};

int main() {
    std::unique_ptr<MyClass> ptr = std::make_unique<MyClass>();
    ptr->print();

    return 0;
}