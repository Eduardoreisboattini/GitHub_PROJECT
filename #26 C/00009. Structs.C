#include <iostream>
#include <string>

struct Person {
    std::string name;
    int age;
};

int main() {
    Person person;
    person.name = "John Doe";
    person.age = 30;

    std::cout << "Name: " << person.name << std::endl;
    std::cout << "Age: " << person.age << std::endl;

    return 0;
}