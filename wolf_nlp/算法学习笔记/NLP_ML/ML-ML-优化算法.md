## NLP_ML - 优化算法
- **概述：**
>       无约束优化算法：
>           在机器学习中的无约束优化算法中，除了梯度下降以外，还有最小二乘，牛顿法，拟牛顿法
>
>       带约束的优化问题：
>           如MaxEnt
>
>

- **梯度下降、最小二乘、牛顿法比较：**
>       梯度 VS 最小二乘：
>           梯度下降法需要选择步长，迭代求解
>           最小二乘不需要选择步长，计算解析解
>           最小二乘优势：
>               如果样本量不算很大，且存在解析解，最小二乘比梯度下降法更有优势，计算速度很快。
>           梯度下降优势：
>               如果样本量很大，最小二乘由于需要一个超级大的逆矩阵，很难或者很慢才能求解析解，使用梯度下降法比较有优势
>
>       梯度下降法 VS 牛顿法/拟牛顿法：
>           梯度下降法是梯度求解，
>           牛顿法/拟牛顿法是二阶Hessian的逆矩阵或伪矩阵求解，
>
>           使用牛顿法/拟牛顿法收敛的更快，但是每次迭代的时间比梯度下降法更长。
>
>
>
>
>
>
>
>

- **待续：**
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
