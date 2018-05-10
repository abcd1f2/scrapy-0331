#include <time.h>
#include <random>
#include <iostream>
using namespace std;

/*
    c++11֮ǰ�������
        srand() �������ӣ���ʼ��rand() 
        rand() ��ȡ�����
        �磺srand(time(NULL));
            rand() ��ȡ�����


    c++11�ṩ�˺ܶ��������ѡ��
        ���ȷֲ���
        uniform_int_distribution          �������ȷֲ�
        uniform_real_distribution        ���������ȷֲ�

        ��Ŭ�����ͷֲ���������yes/no���ֽ��������һ��p��һ��1-p��
        bernoulli_distribution    ��Ŭ���ֲ�
        binomial_distribution     ����ֲ�
        geometry_distribution    ���ηֲ�
        negative_biomial_distribution  ������ֲ�

        Rate-based distributions:
        poisson_distribution ���ɷֲ�
        exponential_distributionָ���ֲ�
        gamma_distribution ٤��ֲ�
        weibull_distribution �������ֲ�
        extreme_value_distribution ��ֵ�ֲ�

        ��̬�ֲ���أ�
        normal_distribution        ��̬�ֲ�
        chi_squared_distribution�����ֲ�
        cauchy_distribution       �����ֲ�
        fisher_f_distribution      ��Ъ��F�ֲ�
        student_t_distribution t�ֲ�

        �ֶηֲ���أ�
        discrete_distribution��ɢ�ֲ�
        piecewise_constant_distribution�ֶγ����ֲ�
        piecewise_linear_distribution�ֶ����Էֲ�
*/

int main()
{
    default_random_engine random(time(NULL));

    //������ķ�ΧΪ[]
    uniform_int_distribution<> uniform(1, 100);
    cout << "uniform_int_distribution " << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << uniform(random) << endl;
    }

    uniform_real_distribution<> uniform2(0.0, 1.0);
    cout << "uniform_real_distribution " << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << uniform2(random) << endl;
    }

    cin.get();
    return 0;
}

