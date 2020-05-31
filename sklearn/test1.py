from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# list = sklearn.datasets.load_iris()

iris = load_iris()

# 训练集特征值，测试集特征值，训练集目标值，测试集目标值
x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

print(x_train.shape)

# 数据集划分


