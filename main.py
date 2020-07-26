import subprocess
import vistas
from usuarios import acciones

"""
Este es el módulo principal del Proyecto de Integración para mejorar hábilidades
en el uso de contenedores con tecnología de Docker.
"""

#def elegirOpcionInicio():



if __name__ == "__main__":

    validacion = True

    while validacion:
        opcion = vistas.inicio()

        try:
            accion = acciones.Acciones()
            subprocess.call('clear')

            if opcion != '1' and opcion != '2' and opcion != '3':
                raise ValueError('OpcionInvalida')

            elif opcion == '1':
                validacion = False
                user = accion.iniciarSesion()
                vistas.seleccionTipoEjercicio(user)

            elif opcion == '2':
                validacion = False
                user = accion.registrarse()
                user = accion.iniciarSesion()
                vistas.seleccionTipoEjercicio(user)
            
            elif opcion == '3':
                validacion = False
                print('¡Hasta Luego!')

        except ValueError as err:
            print('\n¡Opción inválida! :(, intenta otra vez\n')
            continue
    