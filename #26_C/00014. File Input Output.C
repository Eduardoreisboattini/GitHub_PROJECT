#include <iostream>
#include <fstream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "This is some text." << std::endl;
        file.close();
        std::cout << "File written successfully." << std::endl;
    } else {
        std::cerr << "Unable to open file." << std::endl;
    }

    return 0;
}