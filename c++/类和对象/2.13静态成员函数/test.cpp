#include <iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
    void show();
public:
    static int getTotal();  //声明静态成员函数
private:
    static int m_total;  //总人数
private:
    char *m_name;
    int m_age;
    float m_score;
};

int Student::m_total = 0;

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){
    m_total++;
}

void Student::show(){
    cout<<m_name<<"的年龄是"<<m_age<<"，成绩是"<<m_score<<endl;
}

//定义静态成员函数
int Student::getTotal(){
    return m_total;
}

int main(){
    Student *stu1 = new Student("小明", 15, 90.6);
    stu1 -> show();
    Student *stu2 = new Student("小左", 16, 100);
    stu2 -> show();
    int total = Student::getTotal();
    cout<<"当前共有"<<total<<"名学生"<<endl;
    return 0;
}