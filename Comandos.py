# Librerías necesarias
import paramiko
import os

def Comando_por_ssh(ssh_servidor,ssh_puerto,ssh_usuario,ssh_clave,comando):

	# Conectamos al servidor
	conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
	conexion.connect(username = ssh_usuario, password = ssh_clave)
 
	# Abrimos una sesión en el servidor
	canal = conexion.open_session()
	# Ejecutamos el comando, en este caso un sencillo 'ls' para ver
	# el listado de archivos y directorios
	canal.exec_command(comando)

	# Y vamos a ver la salida
	salida = canal.makefile('rb', -1).readlines()
	if salida:
		# Si ha ido todo bien mostramos el listado de directorios
		print(salida)
	else:
		# Si se ha producido algún error lo mostramos
		print(canal.makefile_stderr('rb', -1).readlines())
	conexion.close()


comando=input("Comando:		 ")

# Datos para la conexión SSH
ssh_servidor = input("Servidor:		")
ssh_usuario  = input("Usuario:		")
ssh_clave    = input("Contraseña:	")
ssh_puerto   = 22 # O el puerto SSH que use nuestro servidor
'''comando      = 'yes hola > /dev/pts/0' '''# el comando que vamos a ejecutar en el servidor

Comando_por_ssh(ssh_servidor,ssh_puerto,ssh_usuario,ssh_clave,comando) 

while True:

	Decision=input("	¿Quieres introducir otro comando?	").upper()

	if Decision=='SI':

		comando=input("Comando:		 ")

		Comando_por_ssh(ssh_servidor,ssh_puerto,ssh_usuario,ssh_clave,comando)

	else:

		break