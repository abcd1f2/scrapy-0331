## media-audio signal
- **概述：**
>
>
>
>
>
>
>

- **滤波器：**
>       滤波分经典滤波和现代滤波
>       1、经典滤波：
>           根据傅里叶分析和变换提出的一个工程概念
>           根据高等数学理论，任何一个满足一定条件的信号，都可以被看成是由无限个正弦波叠加而成。
>           是工程信号是不同频率的正弦波线性叠加而成的，组成信号的不同频率的正弦波叫做信号的频率成分或叫做谐波成分。
>           只允许一定频率范围内的信号成分正常通过，而阻止另一部分频率成分通过的电路，叫做经典滤波器或滤波电路。
>       高通滤波器：
>           允许信号中较高频率的成分通过滤波器
>       低通滤波器：
>           允许信号中较低频率的成分通过滤波器
>       带通滤波器：
>           只允许信号中某个频率范围内的成分通过滤波器
>       带阻滤波器：
>           不允许信号中某个频率范围内的成分通过滤波器
>

- **维纳滤波器：**
>       以下仅供参考
>       1、维纳滤波器与自适应滤波是什么关系，与LMS呢？
>           常用的hamming、taylor都是固定的滤波器，滤波器参数需要根据信号进行计算调整的，这一类滤波器都是自适应滤波器
>           维纳滤波器是利用统计参数，实际应用中可能无法得到，需要借助迭代实现，这样就成了一个新框架→自适应滤波器。
>           参数估计呢可以利用梯度下降法迭代逼近，例如常说的LMS就是迭代逼近的一种方式，LMS本身不同于weiner-filter，但迭代结果可以作为wiener-filter的近似。
>       2、维纳滤波器是有限长（FIR-Finite Impulse Response）还是无限长滤波器（IIR-Infinite Impulse Response）？
>           维纳滤波器是大的理论框架，而FIR/IIR只是实现理论的不同途径，故二者均可。
>       3、基于维纳滤波器这个理论框架的应用有哪些？
>           1）自适应是一种解决工程问题的途径，故很多自适应滤波本质都是维纳滤波（不是全部）；
>           2）MVDR谱估计（Minimum variance distortionless response）、广义旁瓣相消GSC（Generalized Sidelobe Canceller ）等都是维纳框架下的应用
>       4、卡尔曼滤波（Kalman）是维纳滤波的一种吗？
>           应该不是，维纳滤波器是线性滤波器，而卡尔曼滤波器据说是非线性
>
>
>

- **加窗原则：**
>       加窗原则，但通常都不能同时满足这两个要求：
>           1、加窗函数时，应使窗函数频谱的主瓣宽度应尽量窄，以获得高的频率分辨能力
>           2、旁瓣衰减应尽量大，以减少频谱拖尾
>       各种窗的差别主要在于集中于主瓣的能量和分散在所有旁瓣的能量之比
>

- **汉明窗：**
>       海明窗也是余弦窗的一种，又称改进的升余弦窗。
>       海明窗与汉宁窗都是余弦窗，只是加权系数不同。
>       海明窗加权的系数能使旁瓣达到更小。分析表明，海明窗的第一旁瓣衰减为一42dB．海明窗的频谱也是由3个矩形时窗的频谱合成，但其旁瓣衰减速度为20dB/（10oct），这比汉宁窗衰减速度慢。
>
>       语音信号一般在10ms到30ms之间，我们可以把它看成是平稳的。为了处理语音信号，我们要对语音信号进行加窗，也就是一次仅处理窗中的数据。
>           因为实际的语音信号是很长的，我们不能也不必对非常长的数据进行一次性处理。明智的解决办法就是每次取一段数据，进行分析，然后再取下一段数据，再进行分析
>
>       怎么仅取一段数据呢？一种方式就是构造一个函数。这个函数在某一区间有非零值，而在其余区间皆为0.汉明窗就是这样的一种函数。
>           它主要部分的形状像sin（x）在0到pi区间的形状，而其余部分都是0.这样的函数乘上其他任何一个函数f，f只有一部分有非零值。
>
>       因为之后我们会对汉明窗中的数据进行FFT，它假设一个窗内的信号是代表一个周期的信号。
>           （也就是说窗的左端和右端应该大致能连在一起）而通常一小段音频数据没有明显的周期性，加上汉明窗后，数据形状就有点周期的感觉了。
>
>       因为加上汉明窗，只有中间的数据体现出来了，两边的数据信息丢失了，所以等会移窗的时候，只会移1/3或1/2窗，这样被前一帧或二帧丢失的数据又重新得到了体现。
>
>       由于直接对信号（加矩形窗）截断会产生频率泄露，为了改善频率泄露的情况，加非矩形窗，一般都是加汉明窗，因为汉明窗的幅频特性是旁瓣衰减较大，主瓣峰值与第一个旁瓣峰值衰减可达40db
>

- **栅栏现象：**
>       栅栏现象，也称栅栏效应，对一函数实行采样，即是抽取采样点上的对应的函数值。
>       其效果如同透过栅栏的缝隙观看外景一样，只有落在缝隙前的少数景象被看到，其余景象均被栅栏挡住而视为零，这种现象称为栅栏效应。
>
>       不管是时域采样还是频域采样，都有相应的栅栏效应。
>           时域栅栏：
>               只是当时域采样满足采样定理时，栅栏效应不会有什么影响。
>           频率栅栏：
>               而频域采样的栅栏效应则影响很大，“挡住”或丢失的频率成分有可能是重要的或具有特征的成分，使信号处理失去意义。
>               解决方法：
>                   减小栅栏效应可用提高采样间隔也就是频率分辨力的方法来解决。
>                   间隔小，频率分辨力高，被“挡住”或丢失的频率成分就会越少。但会增加采样点数，使计算工作量增加。
>              解决此项矛盾可以采用如下方法：
>                   在满足采样定理的前提下，采用频率细化技术（ZOOM），亦可用把时域序列变换成频谱序列的方法。
>

- **待续：**
>       参考：https://www.cnblogs.com/xingshansi/p/6603263.html    自适应滤波：维纳滤波器——FIR及IIR设计
>           https://www.cnblogs.com/lxy2017/p/4049124.html   什么是汉明窗？加Hanmming窗的作用？
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