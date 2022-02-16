def main():
    nombre=input('Dame tu nombre: ')
    apellido_paterno=input('Dame tu apellido paterno: ')
    apellido_materno=input('Dame tu apellido materno: ')
    nombre_completo=nombre+' '+apellido_paterno+' '+apellido_materno
    print(nombre_completo)

if __name__=='__main__':
    main()
