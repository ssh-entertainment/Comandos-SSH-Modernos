# Comandos-SSH-Modernos
ssh {Usuario}@{IP}

apt-get install sshpass (Esto es para poner la contraseña y entrar del tiron)

sshpass -p {Contraseña} ssh {Usuario}@{IP}

Si quieres poner un comando sin entrar en ssh

sshpass -p {Contraseña} ssh {Usuario}@{IP} {Comandos}

La contraseña de Luis es: Estufita

Para romper el Script de luis:
Entra rapido y pon
pkill zenity

Para poner colorines en la terminal:
apt-get install lolcat

Modo de empleo:

echo/yes {palabra} | lolcat

Para echar a alguien:
Who

pkill -9 -t pts/{Num}

Para poner teclas grandes en una pantalla
figlet {Palabra}

Si estan dentro por ssh o tu estas dentro de su terminal, para redirigir estos comandos:

Primero usar ps aux | grep 'pts' para saber que pts estan(Casi siempre pts/0 para anfitrion y pts/1 para invitado),
Segundo realizar:
{Comando} > /dev/pts{Num}



