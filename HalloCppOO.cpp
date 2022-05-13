#include <iostream>
#include <string>

class HalloCppOO {

    std::string halloWeltText;

    public: HalloCppOO() {
        halloWeltText = "Hallo C++ wirklich Objekt-Orientiert !!! \n";
    } 

    void sayHello()    {
        std::cout << halloWeltText;
    }
}; 

int main() {
    HalloCppOO halloCpp;  
    halloCpp.sayHello();  
    return 0;
}
