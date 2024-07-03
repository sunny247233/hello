# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calculate_bmi(height,weight) -> float:
    # height=float(input('身高:'))
    # weight=float(input('体重：'))
    bmi=weight/(height**2)
    return bmi

def health_check(bmi) -> ():
    if 24.9 >= bmi >= 18.5:
        print('不错，请保持')
    elif bmi > 24.9:
        print('减肥啦')
    else:
        print('加油吃吧')

def input_data() -> (float, float):
    height = float(input('height'))
    weight = float(input('weight'))
    return height, weight


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    height, weight = input_data()
    bmi = calculate_bmi(height,weight)
    print(bmi)
    health_check(bmi)
    # print_hi('PyCharm')
    print('test git')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
help(list)