#1.定义目标函数y = 4*x**2 - 100以及其导数。2.选择了初始点x0，学习率learning_rate和迭代次数num_iterations。3.使用梯度下降算法迭代更新x0的值，以找到最小值和最小点。
import numpy as np

# 定义目标函数
def f(x):
    return 4 * x**2 - 100

# 定义目标函数的导数
def gradient(x):
    return 8 * x

# 初始点
x0 = 0.0

# 学习率
learning_rate = 0.1

# 迭代次数
num_iterations = 100

# 梯度下降算法
for i in range(num_iterations):
    gradient_value = gradient(x0)
    x0 = x0 - learning_rate * gradient_value
    

# 打印最小值和最小点
min_value = f(x0)
min_point = x0
print("最小值:", min_value)
print("最小点:", min_point)
