import subprocess, logoUAM
from ejercicios import tipos

def inicio():
    """Muestra pantalla de bienvenida a los usuarios para iniciar sesión
        o registrase en la aplicación
        """

    subprocess.call('clear')
    logo = logoUAM.printLogo()
    print(logo)
    print(' ¡Hola, bienvenid@!')
    print(' Elige la opción que deseas para ingresar a la aplicación:')
    print("""
        1. Iniciar sesión
        2. Registrarse
        3. Salir
    """)
    opcion = input(' Tu opción: ')

    return opcion

def seleccionTipoEjercicio(usuario):
    """Muestra pantalla donde el usuario elige el tipo de ejercicos que quiere
    resolver, así como el avance"""

    subprocess.call('clear')
    logo = logoUAM.printLogo()
    print(logo)
    print(f'¡Hola {usuario.nombre}!,')
    print('A continuación puedes elegir el tipo de ejercicio que quieres realizar')
    print("""
        1. Retos para prácticar comandos de Docker
        2. Troubleshooting en Docker
        3. Ver mis estádisticas
        4. Salir 
    """)

    opcion = input('Tu opción: ')

    #print('\nTu avance actual: ')

    try:
        subprocess.call('clear')
        tipo = tipos.Tipos()

        if int(opcion) < 1 and int(opcion) > 4:
            raise ValueError('OpcionInvalida')

        elif opcion == '1':
            tipo.practicarComandos(usuario)
            seleccionTipoEjercicio(usuario)

        elif opcion == '2':
            tipo.troubleshootingDocker(usuario)
            seleccionTipoEjercicio(usuario)

        elif opcion == '3':
            print(f'¡Vamos a ver tus estádisticas {usuario.nombre}!')
            seleccionTipoEjercicio(usuario)

        elif opcion == '4':
            print(f'¡Hasta luego, {usuario.nombre}!')

    except ValueError:
        print('\n¡Opción inválida! :(, intenta otra vez\n')