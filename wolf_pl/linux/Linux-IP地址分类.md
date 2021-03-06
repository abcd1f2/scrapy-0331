## linux - IP地址分类
- **概述：**
>       IP地址由两部分组成，即网络地址和主机地址，二者是主从关系。！！！！
>       网络地址：
>           表示其属于互联网的哪一个网络
>       主机地址：
>           表示其属于该网络中的哪一台主机
>
>       IP地址的四大类型标识的是网络中的某台主机。IPV4的地址长度为4字节32位，实际中我们用点分十进制记法。
>       IP地址根据网络号和主机号来分，分为A、B、C三类以及特殊地址D、E。全0和全1的保留不用。！！！！
>
>       A、B、C类地址都是单播地址，它们的网络号字段分别是1、2和3位字节长，二者网络号最前面有1~3位的类别位，其数值分为：0、10、110
>
>       A类：
>           (1.0.0.0 ~ 126.0.0.1，默认子网掩码：255.0.0.0或0XFF000000)
>           0xxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx  二进制表示，该类IP地址的最前面为0
>           第一个字节为网络号，后面三个字节为主机号。该类IP地址的最前面为0，所以地址的网络号取值与1~126之间。
>           一般用于大型网络
>       B类：
>           (128.1.0.0 ~ 191.255.0.0，默认子网掩码：255.255.0.0或0XFFFF0000)
>           10xxxxxx xxxxxxxx xxxxxxxx xxxxxxxx  二进制表示，该类IP地址的最前面为"10"
>           前两个字节为网络号，后两个字节为主机号。该类IP地址的最前面为"10"，所以地址的网络号取值与128~191之间
>           一般用于中等规模
>       C类：
>           (192.0.1.0 ~ 223.255.255.0，默认子网掩码：255.255.255.0或者0XFFFFFF00)
>           110xxxxx xxxxxxxx xxxxxxxx xxxxxxxx  二进制表示，该类地址最前面为"110"
>           前三个字节为网络号，最后一个字节为主机号。该类地址最前面为"110"，所以地址的网络号取值与192~223之间。
>           一般用于小型网络
>       D类：
>           1110xxxx xxxxxxxx xxxxxxxx xxxxxxxx  二进制表示
>           是多播地址。该类IP地址的最前面为"1110"，所以地址的网络号取值与224~239之间。一般用于多路广播用户。
>       E类：
>           11110xxx xxxxxxxx xxxxxxxx xxxxxxxx  二进制表示
>           是保留地址。该类地址的最前面是"1111"，所以地址的网络号取值与240~255之间。
>       回送地址：
>           127.0.0.1
>           一般用于测试使用，例如ping 127.0.0.1来测试本机TCP/IP是否正常。
>
>
>

- **子网掩码：**
>       子网掩码是一种用来指明一个IP地址的哪些位标识的是主机所在的子网，以及哪些位标识的是主机的位掩码。
>       子网掩码不能单独使用，它必须结合IP一起使用。子网掩码只有一个作用：将某个IP地址划分成网络地址和主机地址两部分。！！！
>       作用：
>           通过子网掩码可以判断两个IP在不在一个局域网内部
>           子网掩码可以看出有多少位是网络号，有多少位是主机号
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

- **待续：**
>       参考：https://blog.csdn.net/qq_22238021/article/details/80480687   IPv4编址；（IP地址；网络地址和主机地址；子网掩码；网关；广播地址；）
>
>
>
>
>
>
>
>
>
