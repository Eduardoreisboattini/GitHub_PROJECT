#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> ages;

    ages["John"] = 30;
    ages["Jane"] = 25;
    ages["Alice"] = 35;

    for (const auto& pair : ages) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}