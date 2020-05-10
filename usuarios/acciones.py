import logoUAM
import usuarios.usuario as user

class Acciones:

    #Método para registro de nuevos usuarios en la aplicación
    def registrarse(self):
        logo = logoUAM.printLogo()
        print(logo)
        print('### Registro ###')
        print('Introduce tus datos a continuación:\n')
        nombre = input('Nombre: ')
        username = input('Usuario: ')
        password = input('Password: ')

        usuario = user.Usuario(nombre,username,password)
        registro = usuario.insercionBD()

        if registro[0] >= 1:
            print(f'\nRegistrado: {registro[1].nombre}, {registro[1].username}, {registro[1].password}\n')
        else :
            print(f'\nNo se pudo completar el registro. El username «{registro[1].username}» ya existe.\n')

    #Método el inicio de sesión de los usuarios
    def iniciarSesion(self):
        logo = logoUAM.printLogo()
        print(logo)
        print('### Inicio de sesión ###\n')

        try:
            username = input('Usuario: ')
            password = input('Password: ')

            usuario = user.Usuario('',username,password)
            login = usuario.identificarseBD()

            #Valida que el usuario conincide con el de la BD
            if username == login[2]:
                #print(login)
                print(f'\n¡Bienvenid@ {login[1]}!, {login[2]}')
                print(f'\n¡Haz iniciado sesión como {username} y contraseña {password}!\n')
            
            return login

        except:
            print('Datos incorrectos, intentalo más tarde')
            return None
        
        
