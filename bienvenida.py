import os, logoUAM
from usuarios import acciones

def inicio():
    """Muestra pantalla de bienvenida a los usuarios"""

    os.system('clear')
    logo = logoUAM.printLogo()
    print(logo)
    print('Elige la opción que deseas para ingresar a la aplicaciòn:')
    print("""
        1. Iniciar sesión
        2. Registrarse
    """)
    opcion = input('Tu opción: ')

    return opcion


if __name__ == "__main__":

    opcion = inicio()
    accion = acciones.Acciones()

    try:
        os.system('clear')

        if opcion != '1' and opcion != '2':
            raise ValueError('OpcionInvalida')

        elif opcion == '1':
            user = accion.iniciarSesion()
            if user != None:
                print(f'Logueado {user[1]} {user[2]}')
            else:
                print('Falló')

        elif opcion == '2':
            accion.registrarse()

    except ValueError as err:
        print('\n¡Opción inválida! :(, intenta otra vez\n')
    