# Librerías necesarias
import paramiko
import os
 
comando=input("¿Cual es el comando que quieres realizar? ")

# Datos para la conexión SSH
ssh_servidor = '172.22.2.44'
ssh_usuario  = 'luis'
ssh_clave    = '524680.'
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