#include<iostream>
using namespace std;

class Student{
public:
    Student(char *name, int age, float score);
    void show();
public:
    static int m_total;  //静态成员变量
private:
    char *m_name;
    int m_age;
    float m_score;
};

//通过类类访问 static 成员变量
int Student::m_total;

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){
    m_total++;  //操作静态成员变量
}

void Student::show(){
    cout<<m_name<<"的年龄是"<<m_age<<"，成绩是"<<m_score<<"（当前共有"<<m_total<<"名学生）"<<endl;
}

int main() {
    //通过对象来访问 static 成员变量
    Student stu("小明", 15, 92.5f);
    stu.show();
    //通过对象指针来访问 static 成员变量
    Student *pstu = new Student("李华", 16, 96);
    pstu -> show();
    return 0;
}