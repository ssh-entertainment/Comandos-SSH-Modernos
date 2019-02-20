# Librerías necesarias
import paramiko
import os
 
comando=input("¿Cual es el comando que quieres realizar? ")
ssh_servidor=input("¿Cual es la IP? ")
ssh_usuario=input("¿Cual es el usuario? ")
ssh_clave=input("¿Cual es la contraseña? ")
# Datos para la conexión SSH
ssh_puerto   = 22 # O el puerto SSH que use nuestro servidor
'''comando      = 'yes hola > /dev/pts/0' '''# el comando que vamos a ejecutar en el servidor
 
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