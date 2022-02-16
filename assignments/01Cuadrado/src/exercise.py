def main():
    print('Area y perimetro de un cuadrado')
    print('-------------------------------\n')
    lado=float(input('Lado del cuadrado: '))
    perimetro=lado*4
    area=lado**2
    print(f'El perimetro del cuadrado es: {perimetro:.2f}')
    print(f'El area del cuadrado es: {area:.2f}')

if __name__=='__main__':
    main()
