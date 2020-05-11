import os
import vistas
from usuarios import acciones


if __name__ == "__main__":

    accion = acciones.Acciones()
    opcion = vistas.inicio()

    try:
        os.system('clear')

        if opcion != '1' and opcion != '2':
            raise ValueError('OpcionInvalida')

        elif opcion == '1':
            user = accion.iniciarSesion()
            if user != None:
                print(f'Logueado {user[1]} {user[2]}')
                vistas.seleccionTipoEjercicio(user)
                
            else:
                print('Falló')

        elif opcion == '2':
            accion.registrarse()

    except ValueError as err:
        print('\n¡Opción inválida! :(, intenta otra vez\n')
    