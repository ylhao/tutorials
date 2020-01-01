# include <iostream>
using namespace std;

class Student{
public:
    //成员变量
    char *name;
    int age;
    float score;

    //成员函数
    void say(){
        cout<<name<<"的年龄是"<<age<<"，成绩是"<<score<<endl;
    }
};  // 分号不能丢


int main() {
    Student stu1;
    stu1.name = "yilonghao1";
    Student stu2[2];
    stu2[0].name = "yilonghao2_0";
    stu2[1].name = "yilonghao2_1";
    Student *stu3 = new Student;
    Student *stu4 = new Student[100];
    stu3 -> name = "yilonghao_3";
    std::cout << stu1.name << "," << stu1.age << "," << stu1.score << std::endl;
    std::cout << stu2[0].name << "," << stu2[0].age << "," << stu2[0].score << std::endl;
    std::cout << stu2[1].name << "," << stu2[1].age << "," << stu2[1].score << std::endl;
    std::cout << stu3->name << "," << stu3->age << "," << stu3->score << std::endl;
    stu1.say();
    delete stu3; // new,delete成对出现
    delete stu4; // new[],delete成对出现
    return 0;
}


