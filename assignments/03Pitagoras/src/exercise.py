import math


def main():
    print('Calculo Hipotenusa')
    print('-------------------------------\n')
    a = float(input("Ingrese el cateto A: "))
    b = float(input("Ingrese el cateto B: "))
    c = math.sqrt(a**2+b**2)
    print(f'La hipotenusa es: {c:.2f}')


if __name__ == '__main__':
    main()
