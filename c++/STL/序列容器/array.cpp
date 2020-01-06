#include<iostream>
#include<array>
using namespace std;

int main() {
    std::array<double, 100> data1;
    std::array<double, 100> data2 {};
    std::array<double, 10> data3 {0.5, 1.0, 1.5, 2.0};
    data3[3] = data3[0] + data3[1];
    data3[4] = data3.at(0) + data3.at(1);
    data1.fill(3.1415926);
}