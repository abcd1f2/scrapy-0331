## NLP_ML - SVM
- **概述：**
>       从概率的角度上来说，就是使得置信度最小的点置信度最大
>
>
>

- **SVM原理：**
>       对于求min(1/2*w^2)，其实是一个带约束的二次规划问题，是一个凸问题，凸问题就是指不会有局部最优解。
>       目标函数是一个凸优化问题，具体的是一种二次优化问题--目标函数是二次的，约束条件是线性的。这个可用现成的QP(Quadratic Programming)的优化包进行求解。
>       通过Lagrange Duality 变换到对偶变量的优化问题之后，可照找到一种更加有效的方法进行求解--这也是SVM的一大优势，通常情况下，这种方法比直接使用通用的QP优化包要高效很多
>
>       使用拉格朗日乘子法，给每一个约束条件加上一个拉格朗日乘子
>
>

- **SVM的SMO（Sequential Minimal Optimization）**
>       SMO用于优化dual问题
>
>       对于一个二次函数求极值问题，通常情况下有以下方法：
>           1、Gradient Descent，梯度下降法
>           2、Coordinate Descend的变种
>               每次只选择一个维度作为变量，其他的作为常量，从而原始问题就变成一个一元函数，然后针对一元函数求极值，然后反复轮换不同的维度进行迭代
>               但是当有约束条件的时候，就有问题了：
>                   当有约束条件时，当固定一个为变量，其余的为常量，由于约束条件，变量可以直接求出来，优化根本无法继续进行，迭代到下一轮发现根本没有任何进展，一直停留在原始值
>               SMO（Sequential Minimal Optimization）：
>                   一次选择两个坐标进行优化，然后使用约束条件替换其中一个变量，最后就变成了一个一元二次函数带约束条件的求极值问题，就变得容易求解
>
>

- **SVM应用经验：**
>       高斯核的使用增加了模型复杂度，容易引起过拟合。选择合适的核函数以及软边缘参数C就是训练SVM的重要因素。
>           一般来讲，核函数越复杂，模型越偏向于过拟合；C越大模型越偏向于过拟合，反之则拟合不足。
>       超参数：
>           1、参数C
>               参数C是松弛变量的惩罚因子，用惩罚因子C来解决样本偏移的问题。一般比较小，常通过交叉验证获取比较好的C超参数
>               C越大，容易过拟合，C越小，可能欠拟合
>
>           2、gamma参数
>               gamma参数是选择rbf参数作为kernel后，改函数自带的一个参数。
>               隐含地决定了数据隐射到新的特征空间后的分布，gamma越大，支持向量越少，gamma越小，支持向量越多。
>
>               支持向量的个数影响训练和预测的速度。！！！
>
>               gamma越大，函数越胖，越平滑，非线性效能越小，对噪声越不敏感。
>
>               如下图，不同的gamma对应不同的图形，
> ![avatar](https://github.com/nwaiting/wolf-ai/blob/master/wolf_others/pic/nlp_math_svm_params_a.png)
>
>       核函数：
>           SVM中的核函数，能提高模型的feature维度（低维到高维），从而使SVM具有很好的非线性拟合能力
>           1、若使用核函数，一定要对feature做feature scaling
>           2、如果训练集太小，但feature数量n很大，则训练数据不足以拟合复杂的非线性模型，这种情况下只能使用linear-kernel(即fi=xi)，不能用高斯核
>
>

- **核函数选择经验：**
>       一般使用Linear和RBF核，需要注意的是需要对数据归一化处理，这个细节不能忘了！！！！！！
>       一般情况下RBF效果是不会差与Linear，但是时间上RBF会耗费更多，调参会浪费很多时间
>       吴恩达见解：
>           1、如果feature数量很大，跟样本差不多，选用LR或者是Linear Kernel的SVM
>           2、如果feature数量较小，样本数量一般，选用RBF
>           3、如果feature数量小，样本数量多，需要手工添加一些feature变成第一种情况
>       实践经验：
>           Linear核，参数少，速度快，对于一般数据，分类效果已经很理想了
>           RBF核，有足够的时间寻找参数，可以达到更好的效果
>
>

- **对偶：**
>       Lagrangian乘子法：
>           虽然约束条件能够减小搜索空间，但是如果约束条件本身就是比较复杂的形式的话，其实是比较难处理的问题，为此我们希望把带约束的优化问题转化为无约束的优化问题，即Lagrangian乘子法，
>           通过一些系数将约束条件和目标函数结合在一起，然后求取目标函数的最大值
>
>

- **SVM的核函数：**
>       高维空间有一个华丽的名字--"再生核希尔伯特空间"
>       详情参考：http://blog.pluskid.org/?p=723
>

- **KKT条件：**
>       KKT条件是一个线性规划问题能有最优解的充分和必要条件
>
>
>
>
>
>

- **待续：**
>       参考：<<机器学习>> 周志华
>           https://xijunlee.github.io/2017/03/29/sklearn%E4%B8%ADSVM%E8%B0%83%E5%8F%82%E8%AF%B4%E6%98%8E%E5%8F%8A%E7%BB%8F%E9%AA%8C%E6%80%BB%E7%BB%93/      sklearn中SVM调参说明及经验总结
>           http://svmlight.joachims.org/
>           https://www.ibm.com/support/knowledgecenter/zh/SSLVMB_sub/statistics_mainhelp_ddita/spss/base/advanced_statistics_container.html    线性模型、广义线性模型通用特性
>           http://www.blogjava.net/zhenandaci/archive/2009/03/06/258288.html   SVM入门（七）为何需要核函数
>           https://blog.csdn.net/b285795298/article/details/81977271   支持向量机（SVM）从入门到放弃再到掌握
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
