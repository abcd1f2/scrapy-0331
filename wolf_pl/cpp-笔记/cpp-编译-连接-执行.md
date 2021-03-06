## cpp-笔记 - 编译链接执行
- **概述：**
>       程序可以分为几个阶段：
>           1、预处理
>               宏定义展开，头文件展开、条件编译指令等
>           2、编译
>                   (1)、词法分析（可以利用有限状态机实现）
>                   (2)、语法分析（可以采用上下文无关文法和下推自动机实现，最终生成抽象语法树）
>                       语法检测只能保证代码符合语法规则，不能保证语义正确
>                   (3)、语义分析
>                       编译期进行的语义分析都属于静态语义分析，通常包括声明和类型的匹配，类型的转换
>                       会生成具有标识语义的语法树，然后通常会把语法树翻译成一种中间的表示形式，便于进行代码优化
>                   (4)、中间代码生成和优化
>                       (3)中的中间的表示形式就称之为中间代码，常见的形式有三地址码，中间代码的语法和AST的结构有一一对应关系
>                   (5)、目标代码生成和优化
>                       把中间代码翻译成目标代码，目标代码的语法和中间代码的语法也有一一对应关系
>               翻译为平台相关的机器指令，生成汇编代码
>           3、链接
>               生成可执行文件或库文件
>               跨模块调用函数，访问变量时，如何确定访问地址
>               静态链接：
>                   将源文件中用到的库函数与汇编生成的目标文件.o合并生成可执行文件。
>               动态链接：
>           4、装载
>               如何建立可执行文件、虚拟地址、物理地址的映射关系
>           5、执行
>               机器指令如何执行
>
>

- **符号重定位：**
>       本质上来说，符号重定位要解决的是当前编译单元如何访问「外部」符号这个问题
>
>       c/c++ 程序的编译是以文件为单位进行的，因此每个 c/cpp 文件也叫作一个编译单元(translation unit), 源文件先是被编译成一个个目标文件, 再由链接器把这些目标文件组合成一个可执行文件或库，链接的过程，其核心工作是解决模块间各种符号(变量，函数)相互引用的问题，对符号的引用本质是对其在内存中具体地址的引用，因此确定符号地址是编译，链接，加载过程中一项不可缺少的工作，这就是所谓的符号重定位
>
>       链接时符号重定位指的是在链接阶段对符号进行重定位
>       重定位表：
>           编译器编译文件时时，会建立一系列表项，用来记录哪些地方需要在重定位时进行修正，这些表项叫作“重定位表”
>
>       静态链接：
>           链接器在把目标文件合并成一个可执行文件并分配好各段的加载地址后，就可以重新计算那些需要重定位的符号的具体地址了
>
>       动态链接：
>           Linux 下 ELF 主要支持两种方式：
>               1、加载时符号重定位
>                   对于加载时重定位，其原理很简单，它与链接时重定位是一致的，只是把重定位的时机放到了动态库被加载到内存之后，由动态链接器来进行
>                   这些地址在动态库加载完成后会被动态链接器进行重定位，最终修改为正确的地址，这看起来与静态链接时进行重定位是一样的过程
>               2、地址无关代码
>                   ELF引用了一种叫作地址无关代码的实现方案，该解决方案通过对变量及函数的访问加一层跳转来实现，非常的灵活
>
>
>
>

- **编译静态库：**
>       编译生成静态库：
>           使用ar命令将.o文件生成静态链接库
>           ar -crv libadd.a  add.o
>

- **编译动态库：**
>       如果有用到自己编写的动态库的情况，要确保动态库的编译与程序编译的环境一致。！！！
>
>       编译生成动态库：
>           g++ -fPIC -shared -o libadd.so add.cpp
>
>       -shared ：指定生成动态链接库
>       -static ：指定生成静态链接库
>       -fPIC ：表示编译为位置独立的代码，用于编译共享库。目标文件需要创建成位置无关码，念上就是在可执行程序装载它们的时候，它们可以放在可执行程序的内存里的任何地方
>       -Wall ：生成所有警告信息
>       -g ：编译器在编译的时候产生调试信息
>       -ggdb ：此选项将尽可能的生成gdb的可以使用的调试信息
>

- **动态链接库路径：**
>       /etc/ld.so.conf 文件中设置了动态链接库的寻找路径
>       在文件中添加一下需要设置的路径，然后执行 ldconfig 命令
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
>       参考：https://blog.piasy.com/2017/10/24/I-Need-Know-About-Compile-Link-Load-Execute/index.html     编译、链接、装载、运行
>           https://blog.csdn.net/freestyle4568world/article/details/49817799   静态链接库与动态链接库－－－－C/C++
>           https://www.cnblogs.com/catch/p/3857964.html    linux 下动态链接实现原理
>           http://blog.jobbole.com/96225/#namemangling_chs     彻底了解链接器
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
