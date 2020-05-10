import logoUAM
import usuarios.usuario as user

class Acciones:
    """Define los métodos utilizados por los usuarios"""

    def registrarse(self):
        """Método para registro de nuevos usuarios en la aplicación"""

        logo = logoUAM.printLogo()
        print(logo)
        print('### Registro ###')
        print('Introduce tus datos a continuación:\n')
        nombre = input('Nombre: ')
        username = input('Usuario: ')
        password = input('Password: ')

        #Se crea instancia de Usuario y se registra en la BD
        usuario = user.Usuario(nombre,username,password)
        registro = usuario.insercionBD()

        if registro[0] >= 1:
            print(f'\nRegistrado: {registro[1].nombre}, {registro[1].username},' 
                       + f' {registro[1].password}\n')
        else :
            print(f'\nNo se pudo completar el registro. El username'
                    + f' «{registro[1].username}» ya existe.\n')

    def iniciarSesion(self):
        """Método para el inicio de sesión de los usuarios"""
        
        logo = logoUAM.printLogo()
        print(logo)
        print('### Inicio de sesión ###\n')

        try:
            username = input('Usuario: ')
            password = input('Password: ')

            usuario = user.Usuario('',username,password)
            login = usuario.identificarseBD()

            #Valida que los datos del usuario coninciden en la BD
            if username == login[2]:
                #print(login)
                print(f'\n¡Bienvenid@ {login[1]}!, {login[2]}')
                print(f'\n¡Haz iniciado sesión como {username} y contraseña'
                            + f' {password}!\n')
            
            return login

        #Regresa un dato None cuando los datos no hacen match en la BD
        except:
            print('Datos incorrectos, intentalo más tarde')
            return None
        
        
