### 618线搜方法
 1. 其本质就是在1维情况下求解函数最优解。
 2. 0.618的根本原因是能够更多的使用上一步的计算结果。
 3. 线搜函数中包含两个部分： 
    1. 锁定合适的搜索区间
    2. 在区间内寻找最优解
 4. 复杂度：不难发现搜索区间d以0.618倍的速度每次缩小。即复杂度为o(logN)
 5. 本方法参考书籍 **《数值最优化方法》**（北京大学出版社 高立 著）Page：25~28
 6. 由于对python变量的作用域没有进行深入研究，故此采用类方法的形式进行编程，增加可读性。
 
 