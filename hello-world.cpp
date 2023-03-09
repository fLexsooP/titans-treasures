#include <iostream>
#include <string>

class Hello {
    public:
        void say_hello(std::string to) {
            std::cout << "Hello, " << to << "!" << std::endl;
        }
};

int main() {
    Hello hello_obj = Hello();
    hello_obj.say_hello("World");
    hello_obj.say_hello("Main");

    return 0;
}