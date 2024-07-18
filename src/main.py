# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calculate_bmi(height,weight) -> float:
    # height=float(input('身高:'))
    # weight=float(input('体重：'))
    bmi=weight/(height**2)
    return bmi

def health_check(bmi) -> str:
    if 24.9 >= bmi >= 18.5:
        return ('不错，请保持')
    elif bmi > 24.9:
        return('减肥啦')
    else:
        return('加油吃吧')

def input_data() -> (float, float):
    height = float(input('height'))
    weight = float(input('weight'))
    return height, weight


def np_test():
    x = np.array([1,2,3,4,5])
    y = np.array(
        [
            [1,2,3,4],
            [5,6,7,8]
        ]
    )
    z = np.array(
        [
            [
                [1],[1],[1]
            ],
            [
                [11],[11],[11]
            ]
        ]
    )
    print(x.shape)
    print(y.shape)
    print(z.shape)
    print(x.ndim)
    print(y.ndim)
    print(z.ndim)
    print(x.size)
    print(y.size)
    print(z.size)
    print(x.dtype)
    print(y.dtype)
    print(z.dtype)

    x1 = np.arange(10)
    x2 = np.arange(2,10,2)

    x3 = np.ones((2,3))
    x4 = np.ones_like(y)

    x5 = np.zeros((2,3))
    x6 = np.zeros_like(y)

    x7 = np.empty(10)

    x8 = np.full(10,666)
    x9 = np.full_like(y,666)

    x10 = np.random.randn()
    x11 = np.random.randn(2,3)

    A = np.arange(10).reshape(2,5)
    A1= A + 1
    A2 = A * 3
    A3= np.sin(A)
    A4 = np.exp(A)

#   索引
    B = np.arange(10)
    print(B[2],B[5],B[2:4],B[2:-1],B[2:],B[:-3])
    B1 = np.arange(20).reshape(4,5)
    print(B1[2,1],B1[2],B1[:,0])
    print(B1[[0,2,3],[1,3,4]])

    # 随机数
    B2 = np.random.randint(1,100,10)
    print(B2[B2.argsort()[-3:]])
    # 布尔
    C = np.arange(10)
    C1 = C > 5
    print(C1)
    C[C <= 5] = 0
    C[C > 5] = 1
    print(C)
    C2 = np.arange(20).reshape(4,5)
    print(C2 > 5)
    print(C2[C2 > 5])

    # 使用随机函数画图
    dx = np.linspace(-10,10,100)
    # dy = np.sin(dx)
    # plt.plot(dx,dy)
    dy1 = np.sin(dx) + np.random.rand(len(dx))
    plt.plot(dx, dy1)
    plt.show()

    # 统计函数
    E = np.arange(12).reshape(3,4)
    # np.sum(E)
    # np.prod(E)
    # np.cumsum(E)
    # np.cumprod(E)
    # np.min(E)
    # np.max(E)
    # np.percentile(E, [25, 50, 75])
    # np.quantile(E, [0.25,0.5,0.75])
    # E.sum(axis = 0)

    #增加维度
    F = np.arange(5)
    F[np.newaxis,:]
    F[:,np.newaxis]
    np.expand_dims(F, axis=0)
    np.reshape(F, (1, -1))

    return x

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    # 输入身高体重BMI测试
    height, weight = input_data()
    try:
        bmi = calculate_bmi(height,weight)
        print(bmi)
        print(health_check(bmi))
    except ZeroDivisionError:
        print('不能除0')
    except Exception as e:
        print('错误：'+str(e))

    # '''

    ar = np_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
