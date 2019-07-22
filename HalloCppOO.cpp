#include <iostream>
#include <string>
 
class HelloWorld {

    std::string halloWeltText = "Hallo C++ wirklich Objekt-Orientiert !!! \n";
    
    public: HelloWorld() {
    } 
     
    void sayHello()    {
        std::cout << halloWeltText;
    }
}; 
 
int main() {
    HelloWorld a;  
    a.sayHello();  
    return 0;
}