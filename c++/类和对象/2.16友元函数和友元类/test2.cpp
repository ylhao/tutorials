#include <iostream>
using namespace std;

 //提前声明Address类，因为在Student类中有用到，，如果不提前声明，编译器会报错
class Address;

//声明Student类
class Student{
public:
    Student(char *name, int age, float score);
public:
    void show(Address *addr);
private:
    char *m_name;
    int m_age;
    float m_score;
};

//声明Address类
//必须在定义 show() 函数之前声明 Address 类
//这是因为编译器从上到下编译代码，show() 函数体中用到了 Address 的成员 province、city、district
//如果不提前声明，编译器会报错
class Address{
private:
    char *m_province;  //省份
    char *m_city;  //城市
    char *m_district;  //区（市区）
public:
    Address(char *province, char *city, char *district);
    friend void Student::show(Address *addr);  //将Student类中的成员函数show()声明为友元函数
};

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){}

void Student::show(Address *addr){
    cout<<m_name<<"的年龄是 "<<m_age<<"，成绩是 "<<m_score<<endl;
    cout<<"家庭住址："<<addr->m_province<<"省"<<addr->m_city<<"市"<<addr->m_district<<"区"<<endl;
}

//实现Address类
Address::Address(char *province, char *city, char *district){
    m_province = province;
    m_city = city;
    m_district = district;
}

int main(){
    Student stu("小明", 16, 95.5f);
    Address addr("陕西", "西安", "雁塔");
    stu.show(&addr);
    Student *pstu = new Student("小左", 26, 100.0);
    Address *paddr = new Address("北京", "昌平", "回龙观");
    pstu -> show(paddr);
    return 0;
}