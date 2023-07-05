#include <iostream>
#include <string>

class Vehicle {
public:
    std::string brand;

    void honk() {
        std::cout << "Honk honk!" << std::endl;
    }
};

class Car : public Vehicle {
public:
    std::string model;
};

int main() {
    Car car;
    car.brand = "Ford";
    car.model = "Mustang";

    std::cout << "Car: " << car.brand << " " << car.model << std::endl;
    car.honk();

    return 0;
}