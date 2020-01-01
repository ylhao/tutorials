#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
public:
    void show();
    char *getname() const;
    int getage() const;
    float getscore() const;
private:
    char *m_name;
    int m_age;
    float m_score;
};

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){}

void Student::show(){
    cout<<m_name<<"的年龄是"<<m_age<<"，成绩是"<<m_score<<endl;
}

char *Student::getname() const{
    return m_name;
}

int Student::getage() const{
    return m_age;
}

float Student::getscore() const{
    return m_score;
}

int main(){
    const Student stu1("小明", 15, 90.6);
    // stu1 -> show();  # 常对象无法调用类的非const成员
    cout<<stu1.getname()<<"的年龄是"<<stu1.getage()<<"，成绩是"<<stu1.getscore()<<endl;
    Student const *pstu = new Student("小左", 26, 100.0);
    cout<<pstu->getname()<<"的年龄是"<<pstu->getage()<<"，成绩是"<<pstu->getscore()<<endl;
    return 0;
}