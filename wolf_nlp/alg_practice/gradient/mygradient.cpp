#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <iomanip>
using namespace std;

/*
    �򵥵��ݶ������㷨
    �� f(x) = -x^2 + 4x �ļ�ֵ
*/

float grad(float x_old)
{
    return -2.0 * x_old + 4.0; // f(x)�ĵ���
}

void func1()
{
    float x_old = -1.0;     //��ʼֵ��һ����x_newС��ֵ
    float x_new = 0.0;      //�ݶ�������ʼֵ������(0,0)��ʼ
    float alpha = 0.01;     //ѧϰ��(����)
    float presion = 0.0000001;  //����
    int32_t loop_times = 0;
    while (abs(x_old-x_new) > presion) {
        x_old = x_new;
        x_new = x_old + alpha * grad(x_old);
        loop_times++;
    }

    printf("%f\n", x_new);
    //setprecision ���10λ��
    cout << setprecision(10) << x_new << " loop times " << loop_times << endl;
}

int main()
{
    func1();

    cin.get();
    return 0;
}
