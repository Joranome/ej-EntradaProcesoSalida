import math
def main():
    print('Volumen de una esfera')
    print('-------------------------------\n')
    radio=float(input('Radio de la esfera: '))
    volumen=4/3*math.pi*radio**2
    print(f"El volumen de la esfera es: {volumen:.2}")
if __name__=='__main__':
    main()
