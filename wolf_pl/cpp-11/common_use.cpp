#include <iostream>
#include <random>
#include <algorithm>
#include <vector>
#include <inttypes.h>

using namespace std;

/*
    linux���룺g++ common_use.cpp -o common_use -std=c++0x
*/

void func1()
{
    vector<uint32_t> data1;
    for (int i = 0; i < 10; i++) {
        data1.push_back(i);
    }

    //������� c++11֧��
    std::shuffle(data1.begin(), data1.end(), std::default_random_engine(1));
    for (auto& it : data1)
    {
        cout << it << " ";
    }
    cout << endl;
}

int main()
{
    //func1();

    cin.get();
    return 0;
}
