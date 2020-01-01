#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
public:
    friend void show(Student *pstu);  //声明函数为友元函数
private:
    char *m_name;
    int m_age;
    float m_score;
};

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){}

// 全局函数，非成员函数，在友元函数中不能直接访问类的成员，必须要借助对象
void show(Student *pstu){
    cout<<pstu->m_name<<"的年龄是 "<<pstu->m_age<<"，成绩是 "<<pstu->m_score<<endl;
}

int main(){
    Student stu1("小明", 15, 90.6);
    show(&stu1);  //调用友元函数
    Student *pstu = new Student("小左", 26, 100);
    show(pstu);  //调用友元函数
    return 0;
}