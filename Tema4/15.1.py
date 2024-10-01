from HeronsFormula15 import HeronsFormula

if __name__ == '__main__':
    print("Эта программа для вычисления площади с помошью формулы Герона")
    print("Введие числа a,b,c: ")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    print(HeronsFormula(a,b,c))
