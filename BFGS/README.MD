### BFGS 
1. 本方法参考书籍 **《数值最优化方法》**（北京大学出版社 高立 著）Page：76
2. 参数设置参考 数值试验1
3. function2dim2.py 为参考 P76 设置
4. lineSearch.py 为 618 法的精确线搜
5. wolfSearch.py 为 wolf 准则的非精线搜，参数按照 **《数值最优化方法》** P76第二段文字进行设置。实现方法按照 **《计算广告》** （刘鹏 著）中P159页的线搜伪码实现。
5. wolfSearch.py 为 强wolf 准则的非精线搜，有问题，仍在测试中……
6. BFGS.py 的实现参考 **《数值最优化方法》** P59 算法3.4 以及 P63公式 3.32
7. 由于参考资料中并未对 H0 （对称正定）的取值进行过多限制。参考其他内容设置为单位矩阵。
8.  wolf 准则的非精线搜下收敛轨迹基本吻合P77图B
9. 拟牛顿方法的家族中有很多方法，这里就不一一实现。

### 关于线搜
该方法中对线搜进行了多种不同的尝试
