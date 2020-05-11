import os, sys, logoUAM
import subprocess
from time import sleep

def evaluarEjercicio():

    import sys, subprocess

    proceso = subprocess.Popen(['sudo docker ps -a'], stdout=subprocess.PIPE, shell=True)
    proceso.wait()
    salida = proceso.stdout.read()
    proceso.stdout.close()
    salida = salida.decode(sys.getdefaultencoding())

    listSalida = salida.split('\n')

    resultado = False

    for line in listSalida:

        if 'python' in line and '\"sleep 5\"' in line and 'PythonTest' in line:
            #print(line)
            resultado = True

    return resultado


def vistaLevantarDocker(usuario):
    subprocess.call('clear')

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

    input('Comenzar...')
    sleep(1)
    print('Ahora estás en KornShell')

    os.system('sudo docker rm $(sudo docker ps -a | grep "Exited" '
                + '| awk \'{print $NF}\') > null')

    os.system('sudo systemctl stop docker')
    subprocess.call('ksh')

    print('Ya salimos del KornShell')

    resultado = evaluarEjercicio()
    print('\nEvaluando ejercicio...')
    sleep(3)

    if resultado == True:
        print('\n¡Ejercicio Correcto!')
    else:
        print('\n¡Resultado incorrecto!, intenta otra vez')

    sleep(3)
    input()
    resultadoEjercicio = [usuario, resultado]

    return(resultadoEjercicio)   