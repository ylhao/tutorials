#include<iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
    void show();
    char *getname() const;  // 声明常成员函数，在末尾加 const
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

//定义常成员函数，在末尾加 const
char * Student::getname() const{
    return m_name;
}
int Student::getage() const{
    return m_age;
}
float Student::getscore() const{
    return m_score;
}

int main() {
    Student *stu1 = new Student("小左", 26, 100.0);
    stu1 -> show();
    cout << stu1 -> getname() << endl;
    cout << stu1 -> getage() << endl;
    cout << stu1 -> getscore() << endl;
}