#include <iostream>
#include <thread>

void hello() {
    std::cout << "Hello from thread!" << std::endl;
}

int main() {
    std::thread t(hello);
    t.join();

    std::cout << "Hello from main!" << std::endl;

    return 0;
}