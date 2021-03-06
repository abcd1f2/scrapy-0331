## cpp-笔记 - 内存
- **概述：**
>       内存访问越界，向系统申请了一块内存，在使用这块内存的时候，超出了你申请的范围
>
>

- **内存越界可能带来的问题：**
>       1、破坏了堆中的内存分配信息数据，特别是动态分配的内存块的内存信息数据，因为操作系统在分配和释放内存块时需要访问该数据，一旦该数据被破坏
>           *** glibc detected *** free(): invalid pointer:
>           *** glibc detected *** malloc(): memory corruption:
>           *** glibc detected *** double free or corruption (out): 0x00000000005c18a0 ***
>           *** glibc detected *** corrupted double-linked list: 0x00000000005ab150 ***
>       2、破坏了程序自己的其他对象的内存空间，这种破坏会影响程序执行的不正确性，当然也会诱发coredump，如破坏了指针数据
>       3、破坏了空闲内存块，很幸运，这样不会产生什么问题，但谁知道什么时候不幸会降临呢？
>
>       总结：
>           通常，代码错误被激发也是偶然的，也就是说之前你的程序一直正常，可能由于你为类增加了两个成员变量，或者改变了某一部分代码，coredump就频繁发生，而你增加的代码绝不会有任何问题，这时你就应该考虑是否是某些内存被破坏了
>       排查：
>           排查的原则，首先是保证能重现错误，根据错误估计可能的环节，逐步裁减代码，缩小排查空间
>           检查所有的内存操作函数，检查内存越界的可能
>
>       内存越界的常见原因：
>           1、写越界
>               如向10个字节的数组写入了20个字节;内存操作越界
>           2、错误的函数调用
>               如sprintf等fmt中的预定义和实际输入的变量数不一致
>           3、错误的调用方式
>               如用stdcall 的函数指针 调用pascall的函数
>

- **常见的C语言内存错误：**
>       1、指针没有指向一块合法的内存
>           定义了指针变量，但是没有为指针分配内存，即指针没有指向一块合法的内存
>       2、为指针分配的内存太小
>       3、内存分配成功，但并未初始化
>       4、内存越界
>           内存分配成功，且已经初始化，但是操作越过了内存的边界
>       5、内存泄漏
>           用malloc 函数申请0 字节内存，函数并不返回NULL，而是返回一个正常的内存地址。但是你却无法使用这块大小为0 的内存。
>           这好尺子上的某个刻度，刻度本身并没有长度，只有某两个刻度一起才能量出长度。对于这一点一定要小心，因为这时候if（NULL ！= p）语句校验将不起作用。
>       6、内存已经被释放了，但是继续通过指针来使用
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
>       参考：https://blog.csdn.net/love_gaohz/article/details/44746199    内存越界
>           https://blog.csdn.net/li_wen01/article/details/53580358     内存越界问题
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
