## cpp-笔记 - valgrind工具使用
- **概述：**
>
>
>
>
>
>

- **memcheck：**
>
>       Memcheck将内存泄漏分为两种，
>           1、可能的内存泄漏(possibly lost)
>               指仍然存在某个指针能够访问某块内存，但该指针指向的已经不是该内存首地址。
>           2、确定的内存泄漏(definitely lost)
>               指已经不能够访问这块内存，也分为两种：
>               a、直接的(direct)
>                   指没有任何指针指向该内存
>               b、间接的(indirect)
>                   指指向该内存的指针都位于内存泄露处
>
>
>
>
>
>
>
>
>
>

- **待续：**
>       参考：https://www.ibm.com/developerworks/cn/linux/l-cn-valgrind/index.html
>           https://www.cnblogs.com/AndyStudy/p/6409287.html    valgrind原理以及使用
>           https://zhiqiang.org/coding/check-cpp-memory-using-valgrind.html    用valgrind检查C++程序的内存泄漏
>
>
>
>
>
>
>
>
>
>
>
>
>
>
