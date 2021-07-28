from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
# list = sklearn.datasets.load_iris()

# 数据集划分
def datasets_demo():
    iris = load_iris()

    # 训练集特征值，测试集特征值，训练集目标值，测试集目标值
    x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

    # print(x_train.shape)





def dict_demo():

    dicts = [{
        'city': '北京',
        'temperature': 110
    },{
        'city': '上海',
        'temperature': 60
    },{
        'city': '深圳',
        'temperature': 30
    }]

    transfer = DictVectorizer(sparse=False)
    data_new = transfer.fit_transform(dicts)

    print(data_new)
    print(transfer.get_feature_names())


if __name__ == '__main__':
    dict_demo()
