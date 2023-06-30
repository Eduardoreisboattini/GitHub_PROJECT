#include <iostream>
#include <string>

class Animal {
public:
    virtual void makeSound() {
        std::cout << "The animal makes a sound." << std::endl;
    }
};

class Dog : public Animal {
public:
    void makeSound() override {
        std::cout << "The dog barks." << std::endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        std::cout << "The cat meows." << std::endl;
    }
};

int main() {
    Animal* animal = new Animal();
    Animal* dog = new Dog();
    Animal* cat = new Cat();

    animal->makeSound();
    dog->makeSound();
    cat->makeSound();

    delete animal;
    delete dog;
    delete cat;

    return 0;
}