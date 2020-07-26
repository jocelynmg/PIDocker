import logoUAM
import ejercicios.levantarDocker
import ejercicios.ejercicio as ejercicio

class Tipos:
    """Define los tipos de ejercicios que puede hacer el usuario"""

    def practicarComandos(self, usuario):
        logo = logoUAM.printLogo()
        print(logo)
        print(f'Ok {usuario[1]}, vamos a practicar algunos comandos.')
        print('\nElige de la siguiente lista cuál quieres practicar:')

        print("""
        1. Prácticar comando <run>.
        2. Prácticar comando <rm>.
        3. Prácticar más comandos.
        4. Salir.
        """)

        opcion = input("Tu opción: ")
        opcion = opcion

        return True

    def troubleshootingDocker(self, usuario):
        logo = logoUAM.printLogo()
        print(logo)

        print(f'Ok {usuario.nombre}, vamos a realizar algunos ejercicios de'
                + ' troubleshooting')
        print('\nElige de la siguiente lista cuál quieres hacer:')

        print("""
        1. Problema para levantar contenedores.
        2. Segundo problema.
        3. Tercer problema.
        4. Salir.
        """)

        opcion = input("Tu opción: ")
        
        if opcion == '1':
            resultado = ejercicios.levantarDocker.vistaLevantarDocker(usuario)
            print(f'Tu resultado es el siguiente {resultado}')


        return True