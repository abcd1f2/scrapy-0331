#include <iostream>
#include <fstream>
#include <string>
using namespace std;

/*
    fseek���壺
        ����ԭ�ͣ�int fseek(FILE *fp, LONG offset, int origin)
        �������壺fp �ļ�ָ�� offset �����origin�涨��ƫ��λ���� origin ָ���ƶ�����ʼλ�ã�������Ϊ������������� SEEK_SET �ļ���ʼλ�� SEEK_CUR �ļ���ǰλ�� SEEK_END �ļ�����λ��

    tellg()���壺
        tellg() �������������л�ȡλ��
        streampos tellg();//����һ���������������ָ���λ��
        example:streampos pos = tellg();//��tellg()���ص�ָ��λ�ø�ֵ��pos
    seekg()���壺
        seekg()�����������������е�λ��
        istream& seekg(streampos pos);//����ָ�����õ�posλ��
        istream& seekg(streamoff off, ios_base::seekdir way);//����ָ������Ϊway+off������off ����ƫ��ֵ����way�����ַ

        in.seekg(0,ios::end);   //����ַΪ�ļ���������ƫ�Ƶ�ַΪ0������ָ�붨λ���ļ�������
        in.seekg(-sp/3,ios::end); //����ַΪ�ļ�ĩ��ƫ�Ƶ�ַΪ����������ǰ�ƶ�sp/3���ֽ�
        in.seekg(0,ios::beg);   //����ַΪ�ļ�ͷ��ƫ����Ϊ0�����Ƕ�λ���ļ�ͷ
        curpos = in.tellg();  //��ȡ��ǰλ��

        ��ȡ�ļ����ȣ�
            ifs.seekg(std::streamoff(0), std::ios::end);
            return ifs.tellg();
*/

void func1()
{
    ifstream ifs("ReadMe.txt");
    streampos pos = ifs.tellg();
    ifs.seekg(streamoff(0), ios::end);
    cout << "file length " << ifs.tellg() << endl;

    ifs.seekg(pos);
    ifs.seekg(streampos(1000), ios::end);
    cout << "file have " << ifs.tellg() << endl;
}


int main()
{
    func1();

    cin.get();
    return 0;
}
