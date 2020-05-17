import sys, logoUAM
import subprocess
from time import sleep

def evaluarEjercicio():
    resultado = False

    #SE SACA LA LISTA DE LOS DOCKER QUE HAYA EJECUTADO EL USUARIO
    proceso = subprocess.Popen(
        'docker ps -a'.split(),
        stdout = subprocess.PIPE,
        stderr = subprocess.DEVNULL
        )

    proceso.wait()
    salida = proceso.stdout.read()
    proceso.stdout.close()
    salida = salida.decode(sys.getdefaultencoding()).split('\n')

    #EVALUA QUE SE TENGAN LOS PARÁMETROS SOLICITADOS EN EL DOCKER
    for line in salida:

        if 'python' in line and '\"sleep 5\"' in line and 'PythonTest' in line:
            resultado = True
            print('\n¡Ejercicio Correcto!\n')
        else:
            print('\n¡Resultado incorrecto!, intenta otra vez\n')

    return resultado


def vistaLevantarDocker(usuario):
    subprocess.run('clear')

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    Uamito tiene que levantar un Docker de python con el nombre "PythonTest"
    en modo DETACH y que ejecute el comando "sleep 5", pero tiene problemas
    para lograrlo. Ayuda a Uamito a levantar su Docker, una vez que el contendor
    con las características mencionadas se haya ejecutado se dará como bueno
    el ejercicio.

    Escribe 'exit' cuando hayas finalizado o en cualquier momento para regresar 
    a la aplicación principal.
    """
    print(sentencia)

    input('Da enter para comenzar...')

    #SE RECUPERAN LOS IDS DE LOS DOCKER EN ESTADO EXITED
    proceso = subprocess.Popen(
        'docker ps -aq'.split(), 
        stdout = subprocess.PIPE,
        stderr = subprocess.DEVNULL
        )
    proceso.wait()
    ids = proceso.stdout.read()
    proceso.stdout.close()
    ids = ids.decode(sys.getdefaultencoding()).split()

    #SE LIMPIAN LOS CONTENEDORES QUE SE HAYAN EJECUTADO
    for id in ids:
        subprocess.Popen(f'docker rm {id}'.split())

    #SE APAGA EL SERVICIO DE DOCKER
    subprocess.run(
        'sudo systemctl stop docker.service'.split(),
        stderr = subprocess.DEVNULL
        )
    
    #ENTRANDO A KORN SHELL
    print('\nAhora estás en KornShell')
    subprocess.call('ksh')

    #UNA VEZ QUE EL USUARIO ENTRA EXIT EN LA TERMINAL, SE EVALUA EL EJERCICIO
    print('\nEvaluando ejercicio...')
    sleep(1)
    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)
    input('\nDa enter para continuar.\n')

    return(resultadoEjercicio)   